# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_78`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 227
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 145
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punt_Support3 | defense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punt_Support3 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `10` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 65 | START | 65 | 115 |
| ✅ EXACT | `Action_SnapReceive` | Punt_Support3 | `11` | `11` | 95 | END | 95 | 95 |
| ✅ EXACT | `Action_PuntBall` | Punt_Support3 | `11` | `11` | 116 | START | 116 | 136 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 293 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 111 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 745

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_LongSnap` | 65 | 115 | 51 | inferred_complete_timeline |
| `Action_None` | 116 | 391 | 276 | inferred_complete_timeline |
| `Action_None` | 394 | 671 | 278 | inferred_complete_timeline |
| `Action_None` | 675 | 749 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–493
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 65 | 172 | 108 | inferred_complete_timeline |
| `Action_None` | 175 | 234 | 60 | inferred_complete_timeline |
| `Action_None` | 240 | 471 | 232 | inferred_complete_timeline |
| `Action_None` | 476 | 493 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 450 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 193 | 129 | inferred_complete_timeline |
| `Action_None` | 197 | 425 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–429
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 117 | 53 | inferred_complete_timeline |
| `Action_None` | 130 | 183 | 54 | inferred_complete_timeline |
| `Action_None` | 194 | 429 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 134 | 70 | inferred_complete_timeline |
| `Action_None` | 138 | 457 | 320 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 119 | 32 | inferred_complete_timeline |
| `Action_None` | 132 | 236 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 156 | 92 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 227 | 46 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 388 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 162 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 257 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_None` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_None` | 137 | 153 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 189 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 216 | 152 | inferred_complete_timeline |
| `Action_None` | 220 | 276 | 57 | inferred_complete_timeline |
| `Action_None` | 288 | 364 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 229 | 165 | inferred_complete_timeline |
| `Action_None` | 233 | 276 | 44 | inferred_complete_timeline |
| `Action_None` | 280 | 325 | 46 | inferred_complete_timeline |
| `Action_None` | 328 | 412 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–249 | 243 | 4 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–219 | 220 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 15–95 | 78 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 112–321 | 198 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 120–137 | 18 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 168–452 | 285 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 169–745 | 571 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 210–454 | 219 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 232–314 | 79 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 250–438 | 189 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 251–259 | 4 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 287–296 | 10 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 313–328 | 13 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 325–444 | 120 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 331–453 | 123 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 348–378 | 28 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 397–455 | 32 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 426–567 | 136 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 433–714 | 272 | 5 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 434–749 | 315 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 435–623 | 189 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 441–749 | 309 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 446–465 | 20 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 470–508 | 39 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 475–488 | 7 | 2 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 482–483 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 487–489 | 3 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 494–506 | 13 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 516–521 | 6 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 523–749 | 208 | 7 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 529–568 | 33 | 2 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 533–749 | 202 | 4 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 548–560 | 13 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 559–749 | 183 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 565–749 | 185 | 1 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 569–623 | 53 | 2 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 574–749 | 169 | 3 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 581–694 | 108 | 2 | Undefined position; Undefined team |
| `55` | `72` | Position_Unknown | Team_Unknown | 631–706 | 25 | 5 | Undefined position; Undefined team |
| `56` | `73` | Position_Unknown | Team_Unknown | 639–650 | 7 | 2 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 693–739 | 47 | 1 | Undefined position; Undefined team |
| `58` | `80` | Position_Unknown | Team_Unknown | 706–749 | 44 | 1 | Undefined position; Undefined team |
| `59` | `81` | Position_Unknown | Team_Unknown | 707–749 | 43 | 1 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 716–749 | 34 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 738–743 | 6 | 1 | Undefined position; Undefined team |
| `62` | `85` | Position_Unknown | Team_Unknown | 744–749 | 6 | 1 | Undefined position; Undefined team |
| `63` | `86` | Position_Unknown | Team_Unknown | 745–749 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 127 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [65-229] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-412] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-388] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-216] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-364] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-293] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-457] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-450] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-425] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-429] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-471] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-493] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [65-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-391] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-671] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-64] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-306] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-452] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-386] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-421] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-745] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-428] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-314] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-438] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-321] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-444] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-453] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-378] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-408] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-428] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-455] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-443] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-506] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-567] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-617] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-640] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-645] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-714] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-503] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-749] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-623] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-465] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-508] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-488] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-506] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-521] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-623] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-667] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-675] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-682] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-686] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-692] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-749] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-548] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-568] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-600] for track '48' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-612] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-560] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-592] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-597] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-623] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-627] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-636] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-610] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-694] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-635] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-650] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-654] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [689-690] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-706] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-640] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-650] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-739] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-743] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>