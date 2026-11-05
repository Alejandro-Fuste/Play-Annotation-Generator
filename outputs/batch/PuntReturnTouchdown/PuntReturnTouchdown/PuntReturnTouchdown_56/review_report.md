# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_56`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 118
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `1` | `1` | 28 | START | 28 | 103 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 51 | END | 51 | 51 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 104 | START | 104 | 116 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `21` | `21` | 202 | START | 202 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `21` | 210 | START | 210 | 293 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `21` | `21` | 450 | START | 450 | 455 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 241 | 214 | inferred_complete_timeline |
| `Action_None` | 247 | 252 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 271 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 252 | 225 | inferred_complete_timeline |
| `Action_None` | 281 | 290 | 10 | inferred_complete_timeline |
| `Action_None` | 292 | 451 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 89 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_LongSnap` | 28 | 103 | 76 | inferred_complete_timeline |
| `Action_None` | 104 | 243 | 140 | inferred_complete_timeline |
| `Action_None` | 247 | 258 | 12 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 281 | 254 | inferred_complete_timeline |
| `Action_None` | 293 | 419 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 52 | 103 | 52 | inferred_complete_timeline |
| `Action_PuntBall` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 399 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 198 | 171 | inferred_complete_timeline |
| `Action_None` | 205 | 224 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–413
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 282 | 255 | inferred_complete_timeline |
| `Action_None` | 284 | 413 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 479 | 452 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 448 | 421 | inferred_complete_timeline |
| `Action_None` | 454 | 479 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 274 | 247 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 224 | 197 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 479 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 272 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 193 | 166 | inferred_complete_timeline |
| `Action_None` | 195 | 202 | 8 | inferred_complete_timeline |
| `Action_None` | 204 | 280 | 77 | inferred_complete_timeline |
| `Action_None` | 283 | 291 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 307 | 14 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 355 | 43 | inferred_complete_timeline |
| `Action_None` | 357 | 415 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–404
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 199 | 172 | inferred_complete_timeline |
| `Action_None` | 201 | 235 | 35 | inferred_complete_timeline |
| `Action_None` | 238 | 404 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–418 | 419 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–479 | 467 | 6 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 84–262 | 174 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 102–375 | 270 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 108–185 | 78 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 122–479 | 332 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 128–479 | 345 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 135–422 | 262 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 195–410 | 196 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 241–397 | 156 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 280–416 | 137 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 283–371 | 89 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 288–418 | 113 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 292–330 | 22 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 296–460 | 165 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 305–426 | 112 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 378–380 | 3 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 465–479 | 15 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `37` | `47` | 479 | 479 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [28-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-193] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-280] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-307] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-415] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-418] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-281] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-419] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-198] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-224] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-451] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-413] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-399] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-241] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-448] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-404] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-273] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-372] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-185] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-272] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-446] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-435] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-272] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-422] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-265] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-324] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-410] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-397] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-416] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-371] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-309] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-336] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-418] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-460] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-426] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-479] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>