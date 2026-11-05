# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_18`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `38` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `38` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `38` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 30 | START | 30 | 77 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 58 | END | 58 | 58 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 78 | START | 78 | 92 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `38` | `28` | 196 | START | 196 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `38` | `28` | 205 | START | 205 | 228 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `38` | `28` | 644 | START | 644 | 651 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 59 | 30 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 148 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–654
- **Visible Samples:** 644

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 64 | 35 | inferred_complete_timeline |
| `Action_None` | 76 | 654 | 579 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–627
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 30 | 77 | 48 | inferred_complete_timeline |
| `Action_None` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 605 | 514 | inferred_complete_timeline |
| `Action_None` | 607 | 627 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–567
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 549 | 520 | inferred_complete_timeline |
| `Action_None` | 566 | 567 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–522
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 428 | 399 | inferred_complete_timeline |
| `Action_None` | 430 | 434 | 5 | inferred_complete_timeline |
| `Action_None` | 439 | 522 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–597
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 221 | 192 | inferred_complete_timeline |
| `Action_None` | 226 | 597 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–515
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 77 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_None` | 117 | 436 | 320 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 459 | 464 | 6 | inferred_complete_timeline |
| `Action_None` | 499 | 515 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 54 | 25 | inferred_complete_timeline |
| `Action_None` | 63 | 257 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 189 | 160 | inferred_complete_timeline |
| `Action_None` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 659 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 75 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 555 | 526 | inferred_complete_timeline |
| `Action_None` | 557 | 659 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 659 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–625
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 625 | 596 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 134 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 76 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 179 | 150 | inferred_complete_timeline |
| `Action_None` | 183 | 430 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 10–42 | 17 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 60–62 | 3 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 63–226 | 158 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 66–594 | 528 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 69–358 | 290 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 85–659 | 575 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 89–594 | 506 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 94–659 | 566 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 133–601 | 468 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 139–656 | 517 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 147–594 | 448 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 179–659 | 475 | 6 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 182–188 | 7 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 276–508 | 233 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 322–327 | 6 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 341–659 | 314 | 3 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 343–345 | 3 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 357–641 | 283 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 360–369 | 10 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 392–393 | 2 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 403–462 | 4 | 2 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 437–486 | 42 | 2 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 448–481 | 10 | 3 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 450–454 | 4 | 2 | Undefined position; Undefined team |
| `42` | `68` | Position_Unknown | Team_Unknown | 466–470 | 5 | 1 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 476–480 | 5 | 1 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 490–552 | 63 | 1 | Undefined position; Undefined team |
| `45` | `78` | Position_Unknown | Team_Unknown | 530–548 | 19 | 1 | Undefined position; Undefined team |
| `46` | `79` | Position_Unknown | Team_Unknown | 532–533 | 2 | 1 | Undefined position; Undefined team |
| `47` | `80` | Position_Unknown | Team_Unknown | 553–554 | 2 | 1 | Undefined position; Undefined team |
| `48` | `81` | Position_Unknown | Team_Unknown | 557–659 | 103 | 1 | Undefined position; Undefined team |
| `49` | `84` | Position_Unknown | Team_Unknown | 584–659 | 71 | 3 | Undefined position; Undefined team |
| `50` | `88` | Position_Unknown | Team_Unknown | 617–618 | 2 | 1 | Undefined position; Undefined team |
| `51` | `90` | Position_Unknown | Team_Unknown | 618–619 | 2 | 1 | Undefined position; Undefined team |
| `52` | `91` | Position_Unknown | Team_Unknown | 625–651 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `38` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 86 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [30-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-430] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-76] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-597] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-659] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-654] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-428] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-522] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-549] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 93, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [93-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-436] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-464] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-515] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-605] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-627] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-625] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-555] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-659] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-148] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-214] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-136] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-594] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-594] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-434] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-601] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-609] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-656] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-594] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-643] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-508] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-440] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-645] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-615] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-641] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-369] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-455] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-486] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-552] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-548] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-651] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>