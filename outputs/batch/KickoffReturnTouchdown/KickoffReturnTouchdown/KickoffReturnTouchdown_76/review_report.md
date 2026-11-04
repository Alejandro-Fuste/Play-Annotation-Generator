# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_76`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `29` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker3 | defense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 19 | START | 19 | 52 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 53 | START | 53 | 57 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `29` | `23` | 159 | START | 159 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `23` | 190 | START | 190 | 254 |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker3 | `17` | `17` | 548 | START | 548 | 569 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_KickApproach` | 19 | 52 | 34 | inferred_complete_timeline |
| `Action_KickBall` | 53 | 57 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 569 | 512 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 262 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 328 | 310 | inferred_complete_timeline |
| `Action_None` | 331 | 569 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 296 | 278 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 336 | 11 | inferred_complete_timeline |
| `Action_None` | 338 | 385 | 48 | inferred_complete_timeline |
| `Action_None` | 391 | 510 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–514
- **Visible Samples:** 511

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 314 | 296 | inferred_complete_timeline |
| `Action_None` | 319 | 514 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 305 | 287 | inferred_complete_timeline |
| `Action_None` | 307 | 315 | 9 | inferred_complete_timeline |
| `Action_None` | 317 | 321 | 5 | inferred_complete_timeline |
| `Action_None` | 323 | 328 | 6 | inferred_complete_timeline |
| `Action_None` | 335 | 569 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–567
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 93 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 233 | 137 | inferred_complete_timeline |
| `Action_None` | 236 | 567 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_None` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 171 | 126 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 227 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–532
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 11 | 6 | inferred_complete_timeline |
| `Action_None` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_None` | 35 | 292 | 258 | inferred_complete_timeline |
| `Action_None` | 294 | 313 | 20 | inferred_complete_timeline |
| `Action_None` | 319 | 528 | 210 | inferred_complete_timeline |
| `Action_None` | 530 | 532 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 192 | 174 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–467
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 355 | 337 | inferred_complete_timeline |
| `Action_None` | 362 | 467 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 547 | 314 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 548 | 569 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 192 | 174 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 569 | 551 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 342 | 324 | inferred_complete_timeline |
| `Action_None` | 345 | 558 | 214 | inferred_complete_timeline |
| `Action_None` | 562 | 569 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–530
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 513 | 495 | inferred_complete_timeline |
| `Action_None` | 528 | 530 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–562
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 262 | 244 | inferred_complete_timeline |
| `Action_None` | 264 | 562 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 156 | 138 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 189 | 22 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 569 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 173 | 155 | inferred_complete_timeline |
| `Action_None` | 177 | 297 | 121 | inferred_complete_timeline |
| `Action_None` | 323 | 569 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 236 | 218 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 294 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 43–84 | 5 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 61–569 | 509 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 69–264 | 186 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 83–522 | 407 | 8 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 110–137 | 13 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 120–161 | 22 | 4 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 223–510 | 268 | 4 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 238–354 | 41 | 9 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 260–569 | 310 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 261–569 | 309 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 269–569 | 301 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 289–324 | 36 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 307–406 | 100 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [19-513] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-530] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-569] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-355] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-467] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-514] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-296] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-385] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-510] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-567] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-562] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-342] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-558] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-156] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-189] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-547] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-31] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-171] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-292] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-313] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-528] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-569] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [159-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [297-522] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-368] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-510] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-406] for track '33' has 1 frames without a visible bounding box.
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

</details>