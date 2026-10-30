# Play-Annotation-Generator Annotation Review — FieldGoalBlock_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_102`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 43
- **Ball Tracks:** 1
- **Action Segments:** 135
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher5 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `10` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `13` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `8` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 219 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `10` | `10` | 192 | START | 192 | 206 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 220 | START | 220 | 226 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher5 | `16` | `16` | 225 | START | 225 | 243 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_PlaceBall` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_None` | 207 | 254 | 48 | inferred_complete_timeline |
| `Action_None` | 278 | 291 | 14 | inferred_complete_timeline |
| `Action_None` | 298 | 320 | 23 | inferred_complete_timeline |
| `Action_None` | 327 | 479 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_KickBall` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_None` | 227 | 362 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 289 | 70 | inferred_complete_timeline |
| `Action_None` | 302 | 479 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–468
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 167 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 240 | 468 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 219 | 22 | inferred_complete_timeline |
| `Action_None` | 220 | 266 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_None` | 232 | 381 | 150 | inferred_complete_timeline |
| `Action_None` | 383 | 435 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 472 | 253 | inferred_complete_timeline |
| `Action_None` | 474 | 478 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–466
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 445 | 226 | inferred_complete_timeline |
| `Action_None` | 451 | 466 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 439 | 220 | inferred_complete_timeline |
| `Action_None` | 450 | 470 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 257 | 38 | inferred_complete_timeline |
| `Action_None` | 259 | 384 | 126 | inferred_complete_timeline |
| `Action_None` | 397 | 405 | 9 | inferred_complete_timeline |
| `Action_None` | 417 | 430 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–474
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 44 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 118 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 202 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 224 | 21 | inferred_complete_timeline |
| `Action_BlockKick` | 225 | 243 | 19 | inferred_complete_timeline |
| `Action_None` | 244 | 474 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–472
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 259 | 40 | inferred_complete_timeline |
| `Action_None` | 264 | 472 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 323 | 104 | inferred_complete_timeline |
| `Action_None` | 325 | 479 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–460
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_None` | 220 | 460 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–273 | 274 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 2–479 | 478 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 11–472 | 457 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 20–298 | 274 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 52–479 | 312 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 191–465 | 272 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 235–435 | 201 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 239–445 | 74 | 14 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 247–306 | 22 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 247–479 | 233 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 269–281 | 13 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 270–280 | 10 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 280–479 | 200 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 282–329 | 14 | 4 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 285–374 | 89 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 288–479 | 191 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 334–337 | 4 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 337–479 | 140 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 347–350 | 4 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 363–404 | 28 | 3 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 382–411 | 12 | 3 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 383–479 | 97 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 440–472 | 33 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 460–469 | 4 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 460–471 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `28` | 217 | 217 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 110 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [220-472] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-478] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-439] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-470] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-445] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-466] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-362] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-460] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-323] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-381] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-435] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-184] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-468] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-472] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-61] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-141] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-474] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-384] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-405] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-430] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-344] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-463] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-130] for track '22' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-479] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-304] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-382] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-465] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-435] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-262] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-479] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-371] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-479] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-473] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-472] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-471] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>