# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_94`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Personal_Protector1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 106 |
| ✅ EXACT | `Action_LongSnap` | Personal_Protector1 | `0` | `0` | 78 | START | 78 | 114 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 107 | END | 107 | 107 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 133 | START | 133 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | `22` | `21` | 234 | START | 234 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `21` | 261 | START | 261 | 318 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `15` | `15` | 546 | START | 546 | 551 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 98 | 21 | inferred_complete_timeline |
| `Action_None` | 106 | 126 | 21 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 98 | 21 | inferred_complete_timeline |
| `Action_None` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 190 | 16 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 237 | 26 | inferred_complete_timeline |
| `Action_None` | 240 | 254 | 15 | inferred_complete_timeline |
| `Action_None` | 261 | 266 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 307 | 39 | inferred_complete_timeline |
| `Action_None` | 310 | 392 | 83 | inferred_complete_timeline |
| `Action_None` | 394 | 421 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_LongSnap` | 78 | 114 | 37 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–378
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 332 | 255 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 342 | 378 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 107 | 1 | inferred_complete_timeline |
| `Action_None` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 133 | 152 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 307 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 124 | 47 | inferred_complete_timeline |
| `Action_None` | 133 | 146 | 14 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 253 | 42 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 304 | 45 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 139 | 62 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 143 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 207 | 130 | inferred_complete_timeline |
| `Action_None` | 209 | 258 | 50 | inferred_complete_timeline |
| `Action_None` | 260 | 298 | 39 | inferred_complete_timeline |
| `Action_None` | 315 | 341 | 27 | inferred_complete_timeline |
| `Action_None` | 344 | 349 | 6 | inferred_complete_timeline |
| `Action_None` | 359 | 415 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 175 | 98 | inferred_complete_timeline |
| `Action_None` | 202 | 206 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 233 | 156 | inferred_complete_timeline |
| `Action_None` | 258 | 358 | 101 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 177 | 100 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 294 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–326 | 323 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 65–150 | 49 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 90–104 | 15 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 137–569 | 418 | 9 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 141–161 | 21 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 144–355 | 210 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 146–341 | 188 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 168–301 | 132 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 172–381 | 201 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 178–400 | 195 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 179–254 | 76 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 185–384 | 194 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 186–409 | 158 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 216–375 | 128 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 226–231 | 6 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 226–229 | 4 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 232–401 | 166 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 253–365 | 92 | 9 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 262–282 | 21 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 298–343 | 46 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 302–388 | 80 | 4 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 313–362 | 50 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 317–423 | 107 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 332–566 | 235 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 337–389 | 53 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 380–407 | 23 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 500–524 | 19 | 5 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 503–569 | 67 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 510–569 | 60 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 521–569 | 49 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 528–569 | 42 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 530–531 | 2 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 533–569 | 37 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 536–569 | 34 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 547–569 | 9 | 2 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 553–569 | 17 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 557–569 | 13 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 564–569 | 6 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchPunt` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 134 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 189: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_LongSnap' range [78-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-358] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-298] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-341] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-415] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-307] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-392] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-421] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-326] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-139] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-332] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-378] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-134] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-367] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-517] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-521] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 552, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [552-552] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-306] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-355] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-276] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-341] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-301] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-367] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [234-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-340] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [360-400] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-261] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-384] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-289] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-409] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-258] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-375] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-258] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-401] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-367] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-362] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-423] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-566] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-389] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-394] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-407] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-505] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-512] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-553] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>