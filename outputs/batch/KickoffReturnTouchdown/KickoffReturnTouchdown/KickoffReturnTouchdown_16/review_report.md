# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_16`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 100
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
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `18` | `18` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `14` | `14` | 16 | START | 16 | 53 |
| ✅ EXACT | `Action_KickBall` | Kicker | `14` | `14` | 54 | START | 54 | 58 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `18` | `18` | 172 | START | 172 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `18` | `18` | 193 | START | 193 | 546 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `18` | `18` | 547 | START | 547 | 558 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_KickBall` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_None` | 59 | 569 | 511 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 279 | 264 | inferred_complete_timeline |
| `Action_None` | 282 | 569 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 216 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 88 | 73 | inferred_complete_timeline |
| `Action_None` | 90 | 112 | 23 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 272 | 154 | inferred_complete_timeline |
| `Action_None` | 277 | 569 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 569 | 554 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_None` | 211 | 229 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 234 | 219 | inferred_complete_timeline |
| `Action_None` | 236 | 569 | 334 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 214 | 199 | inferred_complete_timeline |
| `Action_None` | 216 | 569 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 377 | 168 | inferred_complete_timeline |
| `Action_None` | 381 | 555 | 175 | inferred_complete_timeline |
| `Action_None` | 557 | 569 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 109 | 94 | inferred_complete_timeline |
| `Action_None` | 113 | 569 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 266 | 251 | inferred_complete_timeline |
| `Action_None` | 268 | 273 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 569 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_CatchKick` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 192 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 546 | 354 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 547 | 558 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 559 | 569 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 194 | 179 | inferred_complete_timeline |
| `Action_None` | 197 | 569 | 373 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 297 | 282 | inferred_complete_timeline |
| `Action_None` | 300 | 569 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–409
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 409 | 394 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 64–569 | 506 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 120–178 | 24 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 155–160 | 6 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 171–193 | 6 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 186–193 | 5 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 194–200 | 6 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 232–569 | 338 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 239–569 | 324 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 344–349 | 5 | 2 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 416–429 | 8 | 3 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 435–569 | 127 | 3 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 459–470 | 4 | 2 | Undefined position; Undefined team |
| `37` | `64` | Position_Unknown | Team_Unknown | 505–509 | 5 | 1 | Undefined position; Undefined team |
| `38` | `68` | Position_Unknown | Team_Unknown | 535–536 | 2 | 1 | Undefined position; Undefined team |
| `39` | `69` | Position_Unknown | Team_Unknown | 535–558 | 16 | 3 | Undefined position; Undefined team |
| `40` | `70` | Position_Unknown | Team_Unknown | 556–558 | 3 | 1 | Undefined position; Undefined team |
| `41` | `71` | Position_Unknown | Team_Unknown | 569–569 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 57 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [16-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-569] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-279] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-409] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-569] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-297] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-377] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-555] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-569] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-483] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-498] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-569] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-509] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-550] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '40' has 1 frames without a visible bounding box.
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

</details>