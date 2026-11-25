# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_5

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_5`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 719
- **Player Tracks:** 70
- **Ball Tracks:** 0
- **Action Segments:** 384
- **Validation Warnings:** 485
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 372
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | Team_Unknown | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `51` | `37` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `51` | `37` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `3` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | `11` | `11` | 129 | START | 129 | 137 |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | `11` | `11` | 183 | START | 183 | 187 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `51` | `37` | 295 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `51` | `37` | 323 | START | 343 | 347 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 34 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 128 | 81 | inferred_complete_timeline |
| `Action_None` | 129 | 168 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 199 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 701

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 274 | 146 | inferred_complete_timeline |
| `Action_None` | 279 | 292 | 14 | inferred_complete_timeline |
| `Action_None` | 296 | 518 | 223 | inferred_complete_timeline |
| `Action_None` | 520 | 666 | 147 | inferred_complete_timeline |
| `Action_None` | 668 | 678 | 11 | inferred_complete_timeline |
| `Action_None` | 680 | 681 | 2 | inferred_complete_timeline |
| `Action_None` | 683 | 684 | 2 | inferred_complete_timeline |
| `Action_None` | 687 | 694 | 8 | inferred_complete_timeline |
| `Action_None` | 699 | 707 | 9 | inferred_complete_timeline |
| `Action_None` | 710 | 719 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 195 | 67 | inferred_complete_timeline |
| `Action_None` | 200 | 219 | 20 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 247 | 7 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 263 | 7 | inferred_complete_timeline |
| `Action_None` | 270 | 281 | 12 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 295 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 310 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–703
- **Visible Samples:** 669

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 168 | 40 | inferred_complete_timeline |
| `Action_None` | 170 | 207 | 38 | inferred_complete_timeline |
| `Action_None` | 215 | 230 | 16 | inferred_complete_timeline |
| `Action_None` | 233 | 252 | 20 | inferred_complete_timeline |
| `Action_None` | 254 | 262 | 9 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_None` | 297 | 377 | 81 | inferred_complete_timeline |
| `Action_None` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_None` | 384 | 654 | 271 | inferred_complete_timeline |
| `Action_None` | 656 | 696 | 41 | inferred_complete_timeline |
| `Action_None` | 699 | 703 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–712
- **Visible Samples:** 698

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 232 | 104 | inferred_complete_timeline |
| `Action_None` | 234 | 258 | 25 | inferred_complete_timeline |
| `Action_None` | 269 | 294 | 26 | inferred_complete_timeline |
| `Action_None` | 296 | 697 | 402 | inferred_complete_timeline |
| `Action_None` | 701 | 712 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–712
- **Visible Samples:** 665

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 310 | 182 | inferred_complete_timeline |
| `Action_None` | 313 | 316 | 4 | inferred_complete_timeline |
| `Action_None` | 320 | 400 | 81 | inferred_complete_timeline |
| `Action_None` | 411 | 413 | 3 | inferred_complete_timeline |
| `Action_None` | 422 | 577 | 156 | inferred_complete_timeline |
| `Action_None` | 580 | 587 | 8 | inferred_complete_timeline |
| `Action_None` | 593 | 596 | 4 | inferred_complete_timeline |
| `Action_None` | 598 | 607 | 10 | inferred_complete_timeline |
| `Action_None` | 609 | 611 | 3 | inferred_complete_timeline |
| `Action_None` | 617 | 693 | 77 | inferred_complete_timeline |
| `Action_None` | 699 | 701 | 3 | inferred_complete_timeline |
| `Action_None` | 708 | 712 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 701

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 295 | 167 | inferred_complete_timeline |
| `Action_None` | 299 | 306 | 8 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 357 | 45 | inferred_complete_timeline |
| `Action_None` | 364 | 458 | 95 | inferred_complete_timeline |
| `Action_None` | 460 | 465 | 6 | inferred_complete_timeline |
| `Action_None` | 471 | 719 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 128 | 60 | inferred_complete_timeline |
| `Action_None` | 129 | 150 | 22 | inferred_complete_timeline |
| `Action_None` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_None` | 178 | 198 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 221 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–713
- **Visible Samples:** 670

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 195 | 67 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 222 | 7 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |
| `Action_None` | 243 | 253 | 11 | inferred_complete_timeline |
| `Action_None` | 255 | 302 | 48 | inferred_complete_timeline |
| `Action_None` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_None` | 322 | 328 | 7 | inferred_complete_timeline |
| `Action_None` | 330 | 689 | 360 | inferred_complete_timeline |
| `Action_None` | 691 | 697 | 7 | inferred_complete_timeline |
| `Action_None` | 705 | 709 | 5 | inferred_complete_timeline |
| `Action_None` | 711 | 713 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 8–287 | 232 | 10 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 17–167 | 21 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 129–472 | 292 | 12 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 165–305 | 139 | 3 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 181–719 | 523 | 9 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 198–213 | 12 | 4 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 199–203 | 5 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 199–204 | 6 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 206–678 | 451 | 11 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 210–216 | 4 | 2 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 214–719 | 496 | 8 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 217–719 | 470 | 11 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 219–240 | 15 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 220–309 | 52 | 7 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 229–712 | 428 | 21 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 230–719 | 447 | 18 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 232–450 | 215 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 241–400 | 65 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 251–719 | 445 | 6 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 296–302 | 7 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 314–719 | 390 | 7 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 317–387 | 63 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 323–597 | 275 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 326–465 | 128 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 343–719 | 370 | 4 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 390–621 | 192 | 17 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 418–719 | 302 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 427–437 | 7 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 474–508 | 18 | 5 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 477–719 | 223 | 12 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 477–719 | 210 | 15 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 486–489 | 4 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 490–491 | 2 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 519–520 | 2 | 1 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 526–719 | 190 | 4 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 527–645 | 119 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 549–643 | 88 | 5 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 554–641 | 75 | 7 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 557–610 | 31 | 8 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 612–642 | 21 | 4 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 613–614 | 2 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 624–710 | 63 | 8 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 629–631 | 3 | 1 | Undefined position; Undefined team |
| `56` | `88` | Position_Unknown | Team_Unknown | 632–678 | 24 | 5 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 632–668 | 23 | 5 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 642–643 | 2 | 1 | Undefined position; Undefined team |
| `59` | `95` | Position_Unknown | Team_Unknown | 653–657 | 5 | 1 | Undefined position; Undefined team |
| `60` | `96` | Position_Unknown | Team_Unknown | 653–659 | 6 | 2 | Undefined position; Undefined team |
| `61` | `98` | Position_Unknown | Team_Unknown | 670–715 | 35 | 5 | Undefined position; Undefined team |
| `62` | `103` | Position_Unknown | Team_Unknown | 680–681 | 2 | 1 | Undefined position; Undefined team |
| `63` | `105` | Position_Unknown | Team_Unknown | 688–709 | 21 | 2 | Undefined position; Undefined team |
| `64` | `106` | Position_Unknown | Team_Unknown | 692–719 | 12 | 5 | Undefined position; Undefined team |
| `65` | `107` | Position_Unknown | Team_Unknown | 692–718 | 21 | 3 | Undefined position; Undefined team |
| `66` | `108` | Position_Unknown | Team_Unknown | 698–701 | 4 | 1 | Undefined position; Undefined team |
| `67` | `109` | Position_Unknown | Team_Unknown | 704–717 | 8 | 3 | Undefined position; Undefined team |
| `68` | `111` | Position_Unknown | Team_Unknown | 709–710 | 2 | 1 | Undefined position; Undefined team |
| `69` | `112` | Position_Unknown | Team_Unknown | 709–710 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_CatchKick` on target `51` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `51` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 7, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '731,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 364 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '37' has invalid range: start=343, end=299. Clamping end to start.
- ⚠️ Action 'Action_None' range [129-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-292] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-518] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-666] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-678] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-681] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-684] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-694] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-707] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-357] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-458] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-465] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-719] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-400] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-577] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-587] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-596] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-607] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-693] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-701] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-712] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-232] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-258] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-294] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-697] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-712] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-219] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-230] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-252] for track '7' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-377] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-654] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-696] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-703] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-60] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-195] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-302] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-689] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-697] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-709] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-713] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [129-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [139-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-245] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-361] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-398] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-458] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-227] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-305] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-407] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-437] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-489] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-586] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-719] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-362] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-405] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-432] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-678] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-425] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-719] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-648] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-653] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-231] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-284] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-421] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-437] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-455] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-515] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-572] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-634] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-650] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-665] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-672] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-684] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-699] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-708] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-712] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-305] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-352] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-455] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-478] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-502] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-618] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-635] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-641] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-675] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-719] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-430] for track '28' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-450] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-327] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-400] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-379] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-537] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-650] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-719] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-374] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-516] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-571] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-595] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-609] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-675] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-387] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-597] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-450] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-347] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-354] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [357-360] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [364-719] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-400] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-421] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-458] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-494] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-530] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-557] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-564] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-576] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-584] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-603] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-610] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-480] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-483] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-500] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-522] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-590] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-608] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-665] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-686] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-482] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-493] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-518] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-528] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-590] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-598] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-617] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-634] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-644] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-697] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-701] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-709] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-719] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-489] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-635] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-662] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-672] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-645] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-556] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-616] for track '49' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-634] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-643] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-584] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-594] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-605] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-613] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-633] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-641] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-559] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-578] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-595] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-623] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-635] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-642] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-643] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-657] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-661] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-666] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-695] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-706] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-631] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-637] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-643] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-646] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-669] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-678] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-638] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-652] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-655] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-662] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-668] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-643] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-657] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-656] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-671] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-678] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-702] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-707] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-715] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-681] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-697] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-709] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-695] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-698] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-716] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-693] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-710] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-718] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-701] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-706] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-710] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-717] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_5'; source metadata written as null.

</details>