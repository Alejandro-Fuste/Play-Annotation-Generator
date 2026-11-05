# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_62`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 719
- **Player Tracks:** 82
- **Ball Tracks:** 0
- **Action Segments:** 184
- **Validation Warnings:** 273
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 168
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `28` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `68` | `45` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `68` | `45` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 41 | START | 41 | 88 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 63 | END | 63 | 63 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 89 | START | 89 | 112 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `28` | `23` | 224 | START | 224 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `68` | `45` | 346 | START | 346 | 674 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `68` | `45` | 675 | START | 675 | 689 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–507
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 209 | 169 | inferred_complete_timeline |
| `Action_None` | 216 | 348 | 133 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_None` | 353 | 507 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 330 | 290 | inferred_complete_timeline |
| `Action_None` | 336 | 365 | 30 | inferred_complete_timeline |
| `Action_None` | 367 | 372 | 6 | inferred_complete_timeline |
| `Action_None` | 374 | 380 | 7 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 419 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 711

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_LongSnap` | 41 | 88 | 48 | inferred_complete_timeline |
| `Action_None` | 89 | 137 | 49 | inferred_complete_timeline |
| `Action_None` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 164 | 719 | 556 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 302 | 262 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–657
- **Visible Samples:** 658

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 657 | 617 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 718

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 89 | 112 | 24 | inferred_complete_timeline |
| `Action_None` | 113 | 486 | 374 | inferred_complete_timeline |
| `Action_None` | 488 | 584 | 97 | inferred_complete_timeline |
| `Action_None` | 586 | 719 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 719 | 679 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 719 | 679 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 719 | 679 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–454
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 339 | 299 | inferred_complete_timeline |
| `Action_None` | 343 | 454 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 133 | 93 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 121 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 65 | 25 | inferred_complete_timeline |
| `Action_None` | 69 | 224 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 236 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 84 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 231 | 191 | inferred_complete_timeline |
| `Action_None` | 238 | 263 | 26 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 148 | 108 | inferred_complete_timeline |
| `Action_None` | 151 | 255 | 105 | inferred_complete_timeline |
| `Action_None` | 257 | 281 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 716

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 650 | 610 | inferred_complete_timeline |
| `Action_None` | 655 | 719 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `22` | Position_Unknown | Team_Unknown | 135–545 | 411 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–506 | 371 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 136–478 | 338 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 142–161 | 20 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 156–719 | 557 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 179–351 | 173 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 245–332 | 88 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 253–332 | 80 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 257–337 | 73 | 6 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 275–326 | 12 | 3 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 282–300 | 12 | 2 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 298–719 | 417 | 4 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 299–301 | 3 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 305–719 | 415 | 1 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 313–538 | 226 | 1 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 321–409 | 43 | 9 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 325–429 | 71 | 5 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 331–339 | 7 | 2 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 331–507 | 177 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 331–332 | 2 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 338–719 | 382 | 4 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 402–547 | 133 | 5 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 406–527 | 121 | 2 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 422–543 | 121 | 2 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 471–560 | 87 | 2 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 483–488 | 6 | 1 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 484–719 | 236 | 1 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 522–555 | 34 | 1 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 528–719 | 189 | 3 | Undefined position; Undefined team |
| `54` | `89` | Position_Unknown | Team_Unknown | 550–577 | 23 | 2 | Undefined position; Undefined team |
| `55` | `90` | Position_Unknown | Team_Unknown | 568–597 | 24 | 2 | Undefined position; Undefined team |
| `56` | `91` | Position_Unknown | Team_Unknown | 569–588 | 20 | 1 | Undefined position; Undefined team |
| `57` | `93` | Position_Unknown | Team_Unknown | 570–597 | 27 | 2 | Undefined position; Undefined team |
| `58` | `94` | Position_Unknown | Team_Unknown | 574–593 | 20 | 1 | Undefined position; Undefined team |
| `59` | `95` | Position_Unknown | Team_Unknown | 575–576 | 2 | 1 | Undefined position; Undefined team |
| `60` | `96` | Position_Unknown | Team_Unknown | 579–585 | 7 | 1 | Undefined position; Undefined team |
| `61` | `97` | Position_Unknown | Team_Unknown | 582–583 | 2 | 1 | Undefined position; Undefined team |
| `62` | `98` | Position_Unknown | Team_Unknown | 591–593 | 3 | 1 | Undefined position; Undefined team |
| `63` | `102` | Position_Unknown | Team_Unknown | 606–719 | 114 | 1 | Undefined position; Undefined team |
| `64` | `103` | Position_Unknown | Team_Unknown | 607–608 | 2 | 1 | Undefined position; Undefined team |
| `65` | `105` | Position_Unknown | Team_Unknown | 619–629 | 7 | 2 | Undefined position; Undefined team |
| `66` | `106` | Position_Unknown | Team_Unknown | 634–639 | 4 | 2 | Undefined position; Undefined team |
| `67` | `107` | Position_Unknown | Team_Unknown | 639–644 | 6 | 1 | Undefined position; Undefined team |
| `68` | `108` | Position_Unknown | Team_Unknown | 641–642 | 2 | 1 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 658–712 | 19 | 2 | Undefined position; Undefined team |
| `70` | `112` | Position_Unknown | Team_Unknown | 659–660 | 2 | 1 | Undefined position; Undefined team |
| `71` | `118` | Position_Unknown | Team_Unknown | 666–719 | 14 | 5 | Undefined position; Undefined team |
| `72` | `123` | Position_Unknown | Team_Unknown | 674–719 | 41 | 2 | Undefined position; Undefined team |
| `73` | `126` | Position_Unknown | Team_Unknown | 685–716 | 25 | 4 | Undefined position; Undefined team |
| `74` | `127` | Position_Unknown | Team_Unknown | 686–719 | 34 | 1 | Undefined position; Undefined team |
| `75` | `128` | Position_Unknown | Team_Unknown | 692–713 | 21 | 2 | Undefined position; Undefined team |
| `76` | `130` | Position_Unknown | Team_Unknown | 693–694 | 2 | 1 | Undefined position; Undefined team |
| `77` | `131` | Position_Unknown | Team_Unknown | 699–719 | 19 | 2 | Undefined position; Undefined team |
| `78` | `132` | Position_Unknown | Team_Unknown | 707–712 | 6 | 1 | Undefined position; Undefined team |
| `79` | `133` | Position_Unknown | Team_Unknown | 707–719 | 13 | 1 | Undefined position; Undefined team |
| `80` | `134` | Position_Unknown | Team_Unknown | 708–713 | 6 | 1 | Undefined position; Undefined team |
| `81` | `137` | Position_Unknown | Team_Unknown | 712–719 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `68` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 63 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 63 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 126 |
| Missing visible bounding boxes during action | 144 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [41-657] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-348] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-507] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-719] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-719] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-330] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-365] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-486] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-584] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-719] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-339] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-454] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-650] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-719] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-302] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-419] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-148] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-281] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-133] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-231] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-236] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-545] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-346] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-506] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-359] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-478] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-524] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-535] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-583] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-719] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-332] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-298] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-510] for track '33' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-623] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-655] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-538] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-345] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-375] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-507] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-424] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-512] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-536] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-521] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-527] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-431] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-543] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-507] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-560] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-555] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-604] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-615] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-719] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-558] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-577] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-583] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-597] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-588] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-594] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-593] for track '58' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-585] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-593] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-621] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-644] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-642] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-668] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-712] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-660] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-668] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [689-690] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-711] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-706] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-691] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-696] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-702] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-716] for track '73' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-697] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-713] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-694] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-714] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [707-712] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-713] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-719] for track '81' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>