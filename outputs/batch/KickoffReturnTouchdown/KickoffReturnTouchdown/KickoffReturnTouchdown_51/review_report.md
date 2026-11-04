# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_51`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 73
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
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Front_Blocker6 | defense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Front_Blocker6 | defense | `3` | `3` |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker6 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `0` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `1` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `15` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `2` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `5` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 80 | START | 80 | 140 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 141 | START | 141 | 145 |
| ✅ EXACT | `Action_CatchKick` | Front_Blocker6 | `3` | `3` | 198 | START | 198 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Front_Blocker6 | `3` | `3` | 211 | START | 211 | 375 |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker6 | `3` | `3` | 376 | START | 376 | 385 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_KickApproach` | 80 | 140 | 61 | inferred_complete_timeline |
| `Action_KickBall` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 278 | 133 | inferred_complete_timeline |
| `Action_None` | 280 | 282 | 3 | inferred_complete_timeline |
| `Action_None` | 285 | 339 | 55 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 373 | 15 | inferred_complete_timeline |
| `Action_None` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 350 | 271 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 366 | 7 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 133 | 54 | inferred_complete_timeline |
| `Action_None` | 135 | 377 | 243 | inferred_complete_timeline |
| `Action_None` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 360 | 281 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 237 | 158 | inferred_complete_timeline |
| `Action_None` | 239 | 310 | 72 | inferred_complete_timeline |
| `Action_None` | 312 | 339 | 28 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 300 | 221 | inferred_complete_timeline |
| `Action_None` | 302 | 389 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 206 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 389 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 225 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 339 | 260 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |
| `Action_None` | 356 | 374 | 19 | inferred_complete_timeline |
| `Action_None` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 354 | 275 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 389 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 370 | 291 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 389 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 343 | 264 | inferred_complete_timeline |
| `Action_None` | 345 | 361 | 17 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_None` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_CatchKick` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 375 | 165 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 376 | 385 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 110–389 | 280 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 207–389 | 179 | 3 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 211–389 | 179 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 211–348 | 135 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 231–389 | 159 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 231–389 | 151 | 4 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 298–389 | 92 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 320–334 | 8 | 2 | Undefined position; Undefined team |
| `26` | `44` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 50 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [80-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-374] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-343] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-361] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-370] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-360] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-278] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-339] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-373] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-389] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-354] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-377] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-350] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-366] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-389] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-339] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-331] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-371] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '25' has 1 frames without a visible bounding box.
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

</details>