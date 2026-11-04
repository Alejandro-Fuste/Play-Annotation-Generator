# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_33`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 154
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `26` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `26` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 12 | START | 12 | 66 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 67 | START | 67 | 72 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `26` | `23` | 186 | START | 186 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `23` | 202 | START | 202 | 298 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `26` | `23` | 556 | START | 556 | 565 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_KickApproach` | 12 | 66 | 55 | inferred_complete_timeline |
| `Action_KickBall` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 73 | 466 | 394 | inferred_complete_timeline |
| `Action_None` | 468 | 569 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 231 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 220 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 237 | 226 | inferred_complete_timeline |
| `Action_None` | 240 | 285 | 46 | inferred_complete_timeline |
| `Action_None` | 289 | 308 | 20 | inferred_complete_timeline |
| `Action_None` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 320 | 325 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 421 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 216 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 163 | 152 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 569 | 388 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 164 | 153 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 196 | 27 | inferred_complete_timeline |
| `Action_None` | 198 | 569 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 283 | 272 | inferred_complete_timeline |
| `Action_None` | 285 | 569 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 109 | 98 | inferred_complete_timeline |
| `Action_None` | 111 | 151 | 41 | inferred_complete_timeline |
| `Action_None` | 154 | 184 | 31 | inferred_complete_timeline |
| `Action_None` | 187 | 323 | 137 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 248 | 237 | inferred_complete_timeline |
| `Action_None` | 251 | 438 | 188 | inferred_complete_timeline |
| `Action_None` | 441 | 524 | 84 | inferred_complete_timeline |
| `Action_None` | 526 | 544 | 19 | inferred_complete_timeline |
| `Action_None` | 546 | 569 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 151 | 140 | inferred_complete_timeline |
| `Action_None` | 153 | 187 | 35 | inferred_complete_timeline |
| `Action_None` | 190 | 218 | 29 | inferred_complete_timeline |
| `Action_None` | 220 | 316 | 97 | inferred_complete_timeline |
| `Action_None` | 318 | 542 | 225 | inferred_complete_timeline |
| `Action_None` | 544 | 562 | 19 | inferred_complete_timeline |
| `Action_None` | 565 | 569 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 262 | 251 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 270 | 273 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 234 | 223 | inferred_complete_timeline |
| `Action_None` | 236 | 280 | 45 | inferred_complete_timeline |
| `Action_None` | 285 | 292 | 8 | inferred_complete_timeline |
| `Action_None` | 296 | 390 | 95 | inferred_complete_timeline |
| `Action_None` | 395 | 468 | 74 | inferred_complete_timeline |
| `Action_None` | 470 | 478 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 520 | 509 | inferred_complete_timeline |
| `Action_None` | 523 | 526 | 4 | inferred_complete_timeline |
| `Action_None` | 532 | 569 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 215 | 204 | inferred_complete_timeline |
| `Action_None` | 217 | 569 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 209 | 198 | inferred_complete_timeline |
| `Action_None` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 438 | 215 | inferred_complete_timeline |
| `Action_None` | 440 | 569 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 18–19 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 115–288 | 172 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 117–569 | 452 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 133–157 | 14 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 139–569 | 427 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 140–294 | 153 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–315 | 135 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 164–569 | 404 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 234–569 | 309 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 243–360 | 66 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 255–567 | 208 | 17 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 307–442 | 131 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 318–569 | 252 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 331–569 | 239 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 346–569 | 224 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 428–430 | 3 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 429–436 | 8 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 432–535 | 54 | 6 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 454–455 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 463–531 | 31 | 8 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 543–569 | 26 | 2 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 561–565 | 5 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 569–569 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 107 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [12-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-520] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-438] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-262] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-196] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-569] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-466] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-234] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-280] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-390] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-468] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-478] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-218] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-316] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-542] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-562] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-151] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-184] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-323] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-283] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-220] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-438] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-524] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-544] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-163] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-308] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-421] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-284] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-322] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-569] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-294] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-289] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-252] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-314] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-302] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-307] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-377] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-426] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-444] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-464] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-495] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-503] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-518] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-442] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-436] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-444] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-462] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-476] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-498] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-515] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-535] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-493] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-558] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-569] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '37' has 1 frames without a visible bounding box.
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

</details>