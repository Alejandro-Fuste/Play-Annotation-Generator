# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_8`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 181
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
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `4` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `22` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `24` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `2` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `4` | `4` | 71 | START | 71 | 125 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 95 | END | 95 | 95 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 126 | START | 126 | 135 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `24` | `22` | 241 | START | 241 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `24` | `22` | 268 | START | 268 | 724 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `24` | `22` | 725 | START | 725 | 732 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 197 | 127 | inferred_complete_timeline |
| `Action_None` | 200 | 304 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 298 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_LongSnap` | 71 | 125 | 55 | inferred_complete_timeline |
| `Action_None` | 126 | 317 | 192 | inferred_complete_timeline |
| `Action_None` | 319 | 350 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 336 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 449 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 183 | 113 | inferred_complete_timeline |
| `Action_None` | 185 | 206 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_None` | 96 | 125 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 126 | 135 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 177 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–409
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 405 | 335 | inferred_complete_timeline |
| `Action_None` | 407 | 409 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–733
- **Visible Samples:** 734

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 733 | 663 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 103 | 33 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 356 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–685
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 685 | 615 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 168 | 98 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 211 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 225 | 155 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 95 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 342 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–742
- **Visible Samples:** 718

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 395 | 325 | inferred_complete_timeline |
| `Action_None` | 421 | 742 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 21–103 | 83 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 102–350 | 241 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 110–165 | 56 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 119–530 | 405 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 166–749 | 584 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 173–749 | 577 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 186–397 | 212 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 193–278 | 86 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 256–262 | 7 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 284–740 | 457 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 289–354 | 66 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 299–511 | 209 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 300–699 | 400 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 355–445 | 91 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 360–735 | 364 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 395–683 | 289 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 397–663 | 224 | 6 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 421–749 | 329 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 449–749 | 300 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 467–722 | 256 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 480–705 | 225 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 486–747 | 258 | 3 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 498–510 | 11 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 511–632 | 119 | 2 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 523–732 | 210 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 523–720 | 181 | 4 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 523–749 | 216 | 3 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 523–553 | 26 | 2 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 541–667 | 121 | 2 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 545–746 | 201 | 2 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 557–720 | 164 | 1 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 599–600 | 2 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 650–719 | 37 | 5 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 650–670 | 15 | 3 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 654–659 | 6 | 1 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 671–672 | 2 | 1 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 676–678 | 3 | 1 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 741–742 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `24` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 96 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [71-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-350] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-395] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-742] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-685] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-405] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-356] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-449] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-733] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-350] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-467] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-530] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-724] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-397] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-740] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-354] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-504] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-699] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-445] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-647] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-655] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-694] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-735] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-683] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-404] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-437] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-569] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-637] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-663] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-658] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-722] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-493] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-705] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-737] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [740-741] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-747] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-502] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-510] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-575] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-632] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-732] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-556] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-720] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-616] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-708] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-543] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-553] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-649] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-667] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-742] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-746] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-720] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-661] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-664] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-669] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-677] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-719] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-654] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-661] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-670] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-659] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-672] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-678] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-742] for track '58' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>