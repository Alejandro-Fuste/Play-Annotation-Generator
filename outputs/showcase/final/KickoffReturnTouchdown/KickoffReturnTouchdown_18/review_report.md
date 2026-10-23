# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_18`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner | defense | `1` | `1` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `15` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `17` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `18` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `19` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `9` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `18` | `18` | 37 | START | 37 | 59 |
| ✅ EXACT | `Action_KickBall` | Kicker | `18` | `18` | 60 | START | 60 | 63 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `1` | `1` | 184 | START | 184 | 189 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner | `1` | `1` | 201 | START | 201 | 486 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner | `1` | `1` | 487 | START | 487 | 509 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_KickApproach` | 37 | 59 | 23 | inferred_complete_timeline |
| `Action_KickBall` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 358 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 189 | 153 | inferred_complete_timeline |
| `Action_None` | 192 | 231 | 40 | inferred_complete_timeline |
| `Action_None` | 242 | 509 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 509 | 473 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 156 | 120 | inferred_complete_timeline |
| `Action_None` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_None` | 171 | 241 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 193 | 157 | inferred_complete_timeline |
| `Action_None` | 195 | 217 | 23 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 261 | 30 | inferred_complete_timeline |
| `Action_None` | 270 | 331 | 62 | inferred_complete_timeline |
| `Action_None` | 333 | 350 | 18 | inferred_complete_timeline |
| `Action_None` | 352 | 509 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–492
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 195 | 159 | inferred_complete_timeline |
| `Action_None` | 198 | 428 | 231 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 434 | 468 | 35 | inferred_complete_timeline |
| `Action_None` | 472 | 480 | 9 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 509 | 473 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 134 | 98 | inferred_complete_timeline |
| `Action_None` | 137 | 334 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 327 | 291 | inferred_complete_timeline |
| `Action_None` | 330 | 364 | 35 | inferred_complete_timeline |
| `Action_None` | 366 | 509 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 316 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 188 | 152 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 255 | 55 | inferred_complete_timeline |
| `Action_None` | 259 | 272 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–508
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 508 | 472 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 306 | 270 | inferred_complete_timeline |
| `Action_None` | 308 | 342 | 35 | inferred_complete_timeline |
| `Action_None` | 349 | 432 | 84 | inferred_complete_timeline |
| `Action_None` | 438 | 509 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 247 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_CatchKick` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 486 | 286 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 487 | 509 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 166 | 130 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 252 | 216 | inferred_complete_timeline |
| `Action_None` | 256 | 509 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 238 | 202 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |
| `Action_None` | 265 | 270 | 6 | inferred_complete_timeline |
| `Action_None` | 272 | 509 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 251 | 215 | inferred_complete_timeline |
| `Action_None` | 257 | 509 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 509 | 473 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–196 | 193 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 65–500 | 431 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 157–509 | 343 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 234–509 | 224 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 243–509 | 267 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 246–342 | 93 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 281–290 | 10 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 299–509 | 211 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 330–509 | 180 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 373–509 | 137 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 475–482 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_None' range [37-306] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-432] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-509] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-428] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-468] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-480] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-188] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-272] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-327] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-364] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-166] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-508] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-189] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-231] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-334] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-358] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-331] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-350] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-258] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-462] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-469] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-476] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-500] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-378] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-497] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-482] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>