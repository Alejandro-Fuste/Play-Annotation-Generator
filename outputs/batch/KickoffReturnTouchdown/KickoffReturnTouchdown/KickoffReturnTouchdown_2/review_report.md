# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_2`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `24` | `21` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `21` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `24` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `8` | `Group` | 0 | START | 0 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `12` | `12` | 8 | START | 8 | 32 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 56 | START | 56 | 60 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `24` | `21` | 171 | START | 171 | 177 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `24` | `21` | 183 | START | 200 | 569 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `24` | `21` | 570 | START | N/A | N/A |

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
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_KickApproach` | 8 | 32 | 25 | inferred_complete_timeline |
| `Action_KickApproach` | 34 | 55 | 22 | inferred_complete_timeline |
| `Action_KickBall` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 66 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 109 | 39 | inferred_complete_timeline |
| `Action_None` | 112 | 318 | 207 | inferred_complete_timeline |
| `Action_None` | 322 | 569 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 318 | 311 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |
| `Action_None` | 338 | 569 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–533
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 116 | 109 | inferred_complete_timeline |
| `Action_None` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |
| `Action_None` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 224 | 62 | inferred_complete_timeline |
| `Action_None` | 231 | 293 | 63 | inferred_complete_timeline |
| `Action_None` | 336 | 384 | 49 | inferred_complete_timeline |
| `Action_None` | 392 | 523 | 132 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |
| `Action_None` | 532 | 533 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 235 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 300 | 293 | inferred_complete_timeline |
| `Action_None` | 302 | 569 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 569 | 477 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 569 | 562 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 167 | 160 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_None` | 178 | 569 | 392 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 61 | 54 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 138 | 72 | inferred_complete_timeline |
| `Action_None` | 140 | 279 | 140 | inferred_complete_timeline |
| `Action_None` | 292 | 569 | 278 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 569 | 562 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 171 | 164 | inferred_complete_timeline |
| `Action_None` | 174 | 183 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 248 | 198 | inferred_complete_timeline |
| `Action_None` | 251 | 283 | 33 | inferred_complete_timeline |
| `Action_None` | 286 | 305 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 278 | 271 | inferred_complete_timeline |
| `Action_None` | 286 | 569 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 30 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 569 | 562 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–566
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 200 | 193 | inferred_complete_timeline |
| `Action_None` | 209 | 339 | 131 | inferred_complete_timeline |
| `Action_None` | 345 | 566 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 257 | 250 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 248 | 241 | inferred_complete_timeline |
| `Action_None` | 256 | 277 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–569 | 566 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–569 | 528 | 8 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 24–28 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 29–569 | 464 | 11 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 31–187 | 156 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 55–117 | 24 | 6 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 71–112 | 37 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 110–115 | 4 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 118–121 | 4 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 126–276 | 147 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 208–569 | 362 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 249–303 | 54 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 275–552 | 271 | 5 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 289–393 | 105 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 289–547 | 259 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 302–336 | 35 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 305–569 | 265 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 306–569 | 264 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 326–569 | 244 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 389–471 | 83 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 401–405 | 5 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 426–427 | 2 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 454–455 | 2 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 465–469 | 5 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 481–493 | 6 | 2 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 491–493 | 3 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `12` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `24` (Position_Unknown): Annotated start 183 != Inferred start 200
- ❌ Missing segment for action `Action_CrossGoalLine` on target `24` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 6: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '21' has invalid range: start=570, end=569. Clamping end to start.
- ⚠️ Action 'Action_None' range [8-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-569] for track '1' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-116] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-224] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-384] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-523] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-178] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-300] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-138] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-279] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-167] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-569] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-569] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-569] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-318] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-257] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [8-32] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [56-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-109] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-318] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-569] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-339] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-566] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-248] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-158] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [171-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-569] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-100] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-158] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-311] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-547] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-393] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-547] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-336] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-471] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 570. Video range is [0, 569].

</details>