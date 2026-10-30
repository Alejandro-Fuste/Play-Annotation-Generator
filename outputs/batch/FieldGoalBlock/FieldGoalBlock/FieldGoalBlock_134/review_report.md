# Play-Annotation-Generator Annotation Review — FieldGoalBlock_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_134`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 213
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 160
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `1` | `1` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Right_Edge_Rusher | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `1` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `13` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `1` | `1` | 34 | START | 34 | 46 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 56 | START | 56 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Right_Edge_Rusher | `9` | `9` | 60 | START | 60 | 60 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PlaceBall` | 34 | 46 | 13 | inferred_complete_timeline |
| `Action_None` | 47 | 203 | 157 | inferred_complete_timeline |
| `Action_None` | 207 | 323 | 117 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_None` | 329 | 333 | 5 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 401 | 403 | 3 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |
| `Action_None` | 430 | 433 | 4 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_KickBall` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 172 | 112 | inferred_complete_timeline |
| `Action_None` | 176 | 204 | 29 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 229 | 14 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 246 | 8 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_None` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_None` | 80 | 321 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 41 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 56 | 386 | 331 | inferred_complete_timeline |
| `Action_None` | 403 | 449 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 55 | 49 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 84 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 449 | 394 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 215 | 160 | inferred_complete_timeline |
| `Action_None` | 217 | 250 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 337 | 282 | inferred_complete_timeline |
| `Action_None` | 339 | 362 | 24 | inferred_complete_timeline |
| `Action_None` | 367 | 425 | 59 | inferred_complete_timeline |
| `Action_None` | 432 | 449 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 173 | 118 | inferred_complete_timeline |
| `Action_None` | 175 | 273 | 99 | inferred_complete_timeline |
| `Action_None` | 275 | 279 | 5 | inferred_complete_timeline |
| `Action_None` | 304 | 307 | 4 | inferred_complete_timeline |
| `Action_None` | 309 | 351 | 43 | inferred_complete_timeline |
| `Action_None` | 360 | 365 | 6 | inferred_complete_timeline |
| `Action_None` | 378 | 424 | 47 | inferred_complete_timeline |
| `Action_None` | 426 | 449 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 259 | 204 | inferred_complete_timeline |
| `Action_None` | 267 | 274 | 8 | inferred_complete_timeline |
| `Action_None` | 277 | 449 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 93 | 38 | inferred_complete_timeline |
| `Action_None` | 100 | 297 | 198 | inferred_complete_timeline |
| `Action_None` | 304 | 397 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 90 | 35 | inferred_complete_timeline |
| `Action_None` | 95 | 449 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 85 | 30 | inferred_complete_timeline |
| `Action_None` | 88 | 374 | 287 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 449 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–394
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 153 | 98 | inferred_complete_timeline |
| `Action_None` | 160 | 208 | 49 | inferred_complete_timeline |
| `Action_None` | 212 | 394 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BlockKick` | 60 | 60 | 1 | inferred_complete_timeline |
| `Action_BlockKick` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_BlockKick` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 188 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 3–51 | 49 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 20–311 | 291 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 23–79 | 38 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 29–449 | 405 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 50–449 | 400 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 51–449 | 380 | 7 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 58–449 | 383 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 58–71 | 4 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 73–343 | 267 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 102–449 | 348 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 156–220 | 24 | 6 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 179–185 | 5 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 187–449 | 252 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 208–228 | 20 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 256–277 | 21 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 262–449 | 182 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 275–278 | 4 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 278–320 | 20 | 3 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 292–316 | 11 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 294–429 | 75 | 12 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 297–336 | 20 | 4 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 314–449 | 136 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 367–449 | 80 | 4 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 383–449 | 65 | 2 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 389–449 | 61 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 393–449 | 53 | 2 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 417–430 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 146 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [61-172] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-203] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-323] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-273] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-424] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-394] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-337] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-362] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-425] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-259] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-215] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' for track '9' starts at frame 60, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockKick' range [60-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [62-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [56-449] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-93] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-397] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-386] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [56-62] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-55] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-84] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-51] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-260] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-311] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-51] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [56-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-449] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-102] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-204] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-88] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-333] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-294] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-436] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-272] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-449] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-320] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-317] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-399] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-420] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-424] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-440] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-401] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-449] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-430] for track '49' has 1 frames without a visible bounding box.
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

</details>