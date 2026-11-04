# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_19`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 214
- **Validation Warnings:** 275
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 202
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `29` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `25` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `29` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `10` | `10` | 12 | START | 12 | 59 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 60 | START | 60 | 64 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `29` | `25` | 174 | START | 174 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `25` | 195 | START | 195 | 393 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `29` | `25` | 510 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_KickApproach` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_KickBall` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 65 | 331 | 267 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 172 | 85 | inferred_complete_timeline |
| `Action_None` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 195 | 509 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 77 | 66 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 356 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 90 | 79 | inferred_complete_timeline |
| `Action_None` | 92 | 164 | 73 | inferred_complete_timeline |
| `Action_None` | 166 | 204 | 39 | inferred_complete_timeline |
| `Action_None` | 206 | 225 | 20 | inferred_complete_timeline |
| `Action_None` | 229 | 252 | 24 | inferred_complete_timeline |
| `Action_None` | 255 | 373 | 119 | inferred_complete_timeline |
| `Action_None` | 377 | 454 | 78 | inferred_complete_timeline |
| `Action_None` | 475 | 477 | 3 | inferred_complete_timeline |
| `Action_None` | 480 | 481 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 486 | 3 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |
| `Action_None` | 494 | 509 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 53 | 42 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 150 | 139 | inferred_complete_timeline |
| `Action_None` | 152 | 175 | 24 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 509 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 47 | 36 | inferred_complete_timeline |
| `Action_None` | 49 | 233 | 185 | inferred_complete_timeline |
| `Action_None` | 236 | 509 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 178 | 167 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 200 | 220 | 21 | inferred_complete_timeline |
| `Action_None` | 222 | 331 | 110 | inferred_complete_timeline |
| `Action_None` | 333 | 465 | 133 | inferred_complete_timeline |
| `Action_None` | 473 | 509 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 232 | 221 | inferred_complete_timeline |
| `Action_None` | 234 | 287 | 54 | inferred_complete_timeline |
| `Action_None` | 291 | 487 | 197 | inferred_complete_timeline |
| `Action_None` | 489 | 509 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 404 | 393 | inferred_complete_timeline |
| `Action_None` | 408 | 411 | 4 | inferred_complete_timeline |
| `Action_None` | 417 | 509 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 482 | 471 | inferred_complete_timeline |
| `Action_None` | 484 | 509 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 410 | 399 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |
| `Action_None` | 421 | 446 | 26 | inferred_complete_timeline |
| `Action_None` | 448 | 509 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 229 | 218 | inferred_complete_timeline |
| `Action_None` | 231 | 298 | 68 | inferred_complete_timeline |
| `Action_None` | 302 | 330 | 29 | inferred_complete_timeline |
| `Action_None` | 333 | 509 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 175 | 164 | inferred_complete_timeline |
| `Action_None` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 3–163 | 152 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–509 | 418 | 9 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 13–14 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 29–234 | 166 | 11 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 47–48 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 53–92 | 31 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 79–83 | 5 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 82–509 | 408 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–509 | 411 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 98–259 | 154 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 101–509 | 407 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 131–509 | 365 | 10 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 131–509 | 379 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 173–509 | 334 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 262–417 | 146 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 264–509 | 239 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 344–410 | 64 | 4 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 369–509 | 119 | 5 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 369–388 | 14 | 3 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 372–382 | 5 | 2 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 376–489 | 53 | 7 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 396–400 | 5 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 397–487 | 82 | 4 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 402–411 | 10 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 404–501 | 38 | 11 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 406–509 | 101 | 3 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 412–414 | 3 | 1 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 419–424 | 5 | 2 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 424–475 | 39 | 4 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 446–448 | 3 | 1 | Undefined position; Undefined team |
| `53` | `85` | Position_Unknown | Team_Unknown | 458–494 | 15 | 4 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 460–498 | 18 | 5 | Undefined position; Undefined team |
| `55` | `89` | Position_Unknown | Team_Unknown | 479–480 | 2 | 1 | Undefined position; Undefined team |
| `56` | `91` | Position_Unknown | Team_Unknown | 506–508 | 3 | 1 | Undefined position; Undefined team |
| `57` | `92` | Position_Unknown | Team_Unknown | 508–509 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (7 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `29` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 184 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '25' has invalid range: start=510, end=509. Clamping end to start.
- ⚠️ Action 'Action_None' range [12-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-298] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-509] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-487] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-410] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-446] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-509] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-404] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-509] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-482] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-509] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-175] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-356] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-178] for track '7' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-465] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-509] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-204] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-225] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-373] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-454] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-233] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-331] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-509] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-509] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-182] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-250] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-349] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-504] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-181] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-80] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-371] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-457] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-476] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-171] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-440] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-509] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-393] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [397-440] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [442-461] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [463-468] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [473-484] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [487-490] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [494-509] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-509] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-302] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-346] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-413] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-509] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-393] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-410] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-430] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-470] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-480] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-494] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-383] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-386] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-406] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-428] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-486] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-428] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-487] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-411] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-451] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-464] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-450] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-421] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-427] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-460] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-465] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-494] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-467] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-476] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 510. Video range is [0, 509].

</details>