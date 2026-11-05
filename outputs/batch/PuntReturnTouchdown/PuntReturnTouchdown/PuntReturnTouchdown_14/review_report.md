# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_14`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 76
- **Ball Tracks:** 0
- **Action Segments:** 203
- **Validation Warnings:** 293
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 189
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | Team_Unknown | `23` | `17` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `33` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `64` | `48` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 3 | START | 3 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 3 | START | 3 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 3 | START | 3 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 3 | START | 3 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 3 | START | 3 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 3 | START | 3 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 3 | START | 3 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `9` | `9` | 106 | START | 106 | 135 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `13` | `13` | 134 | END | 134 | 134 |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | `23` | `17` | 168 | START | 168 | 181 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `33` | `25` | 295 | START | 295 | 309 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `33` | `25` | 310 | START | 310 | 339 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `64` | `48` | 722 | START | 722 | 728 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–110
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 91 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–749
- **Visible Samples:** 736

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 140 | 35 | inferred_complete_timeline |
| `Action_None` | 143 | 462 | 320 | inferred_complete_timeline |
| `Action_None` | 468 | 596 | 129 | inferred_complete_timeline |
| `Action_None` | 601 | 749 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–357
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_LongSnap` | 106 | 135 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 294 | 127 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 350 | 38 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–247
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 247 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–291
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 174 | 69 | inferred_complete_timeline |
| `Action_None` | 176 | 291 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–153
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 133 | 131 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 134 | 1 | inferred_complete_timeline |
| `Action_None` | 135 | 153 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–123
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 123 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–323
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 323 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 161 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–209
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 144 | 39 | inferred_complete_timeline |
| `Action_None` | 150 | 200 | 51 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–111
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–530
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 158 | 53 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 284 | 113 | inferred_complete_timeline |
| `Action_None` | 287 | 380 | 94 | inferred_complete_timeline |
| `Action_None` | 383 | 464 | 82 | inferred_complete_timeline |
| `Action_None` | 466 | 470 | 5 | inferred_complete_timeline |
| `Action_None` | 472 | 473 | 2 | inferred_complete_timeline |
| `Action_None` | 475 | 493 | 19 | inferred_complete_timeline |
| `Action_None` | 503 | 530 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–9
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 9 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–462
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 105 | 103 | inferred_complete_timeline |
| `Action_None` | 106 | 215 | 110 | inferred_complete_timeline |
| `Action_None` | 223 | 433 | 211 | inferred_complete_timeline |
| `Action_None` | 441 | 462 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 15–209 | 155 | 7 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 27–338 | 312 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 133–521 | 372 | 4 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 157–439 | 259 | 8 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 177–208 | 32 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 178–749 | 482 | 5 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 192–373 | 182 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 201–204 | 4 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 208–268 | 61 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 213–361 | 128 | 5 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 217–470 | 253 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 222–231 | 5 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 224–464 | 229 | 7 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 235–336 | 100 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 246–281 | 36 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 249–472 | 224 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 249–473 | 220 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 278–466 | 187 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 282–535 | 238 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 287–464 | 178 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 292–501 | 210 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 300–525 | 223 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 304–482 | 162 | 6 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 328–335 | 8 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 332–346 | 7 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 350–624 | 275 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 370–531 | 139 | 5 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 374–493 | 118 | 2 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 375–521 | 146 | 2 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 379–447 | 66 | 3 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 434–480 | 47 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 438–700 | 245 | 4 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 445–749 | 293 | 9 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 465–571 | 107 | 1 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 465–469 | 5 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 483–680 | 185 | 3 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 511–544 | 34 | 1 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 516–550 | 35 | 1 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 539–749 | 159 | 4 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 565–713 | 141 | 6 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 565–749 | 160 | 4 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 570–726 | 136 | 5 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 573–749 | 177 | 1 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 582–607 | 26 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 589–590 | 2 | 1 | Undefined position; Undefined team |
| `62` | `88` | Position_Unknown | Team_Unknown | 633–749 | 106 | 3 | Undefined position; Undefined team |
| `63` | `89` | Position_Unknown | Team_Unknown | 661–749 | 84 | 2 | Undefined position; Undefined team |
| `64` | `90` | Position_Unknown | Team_Unknown | 667–692 | 26 | 1 | Undefined position; Undefined team |
| `65` | `91` | Position_Unknown | Team_Unknown | 673–749 | 72 | 2 | Undefined position; Undefined team |
| `66` | `92` | Position_Unknown | Team_Unknown | 684–749 | 66 | 1 | Undefined position; Undefined team |
| `67` | `93` | Position_Unknown | Team_Unknown | 692–749 | 58 | 1 | Undefined position; Undefined team |
| `68` | `94` | Position_Unknown | Team_Unknown | 699–749 | 51 | 1 | Undefined position; Undefined team |
| `69` | `95` | Position_Unknown | Team_Unknown | 699–749 | 44 | 2 | Undefined position; Undefined team |
| `70` | `96` | Position_Unknown | Team_Unknown | 713–732 | 20 | 1 | Undefined position; Undefined team |
| `71` | `97` | Position_Unknown | Team_Unknown | 727–728 | 2 | 1 | Undefined position; Undefined team |
| `72` | `101` | Position_Unknown | Team_Unknown | 731–749 | 19 | 1 | Undefined position; Undefined team |
| `73` | `102` | Position_Unknown | Team_Unknown | 738–749 | 12 | 1 | Undefined position; Undefined team |
| `74` | `103` | Position_Unknown | Team_Unknown | 744–749 | 6 | 1 | Undefined position; Undefined team |
| `75` | `106` | Position_Unknown | Team_Unknown | 745–749 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `33` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ 62 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 62 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 124 |
| Missing visible bounding boxes during action | 166 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [106-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-433] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-462] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-91] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-323] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-462] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-596] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-284] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-380] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-464] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-493] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-530] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [106-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-294] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-350] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-247] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-291] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-338] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-326] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-470] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-521] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-344] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-391] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-434] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-436] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-468] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-553] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-373] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-268] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-339] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [359-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-344] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-470] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-337] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-362] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-379] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-436] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-450] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-264] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-336] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-472] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-405] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-430] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-462] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-473] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-454] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-466] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-505] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-535] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-464] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-501] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-460] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-525] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-451] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-470] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-482] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-335] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-624] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-417] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-434] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-510] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-436] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-493] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-489] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-521] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-411] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-423] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-447] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-480] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-506] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-533] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-621] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-700] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-525] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-615] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [617-618] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [620-667] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [669-676] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [681-684] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-571] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-580] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-586] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-680] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-544] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-550] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-649] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-747] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-570] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-612] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-646] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-662] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-707] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-713] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-677] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-691] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-702] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-583] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-618] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-652] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-726] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-607] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-670] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-681] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-675] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-692] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-685] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-749] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-732] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-732] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-728] for track '71' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>