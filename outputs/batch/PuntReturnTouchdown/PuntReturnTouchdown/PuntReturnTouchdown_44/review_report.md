# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_44`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 215
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
- **Inferred Coverage Segments (Action_None):** 158
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `31` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher5 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 38 | START | 38 | 71 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 66 | END | 66 | 66 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 72 | START | 72 | 106 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `31` | `25` | 210 | START | 210 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `25` | 224 | START | 224 | 368 |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher5 | `14` | `14` | 460 | START | 460 | 474 |

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
- **Visible Frames:** 0–80
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 50 | 13 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 212 | 112 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_LongSnap` | 38 | 71 | 34 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 479 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 479 | 442 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 479 | 442 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 387 | 350 | inferred_complete_timeline |
| `Action_None` | 390 | 479 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_None` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_PuntBall` | 72 | 106 | 35 | inferred_complete_timeline |
| `Action_None` | 107 | 357 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 58 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 322 | 285 | inferred_complete_timeline |
| `Action_None` | 332 | 470 | 139 | inferred_complete_timeline |
| `Action_None` | 474 | 479 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 75 | 38 | inferred_complete_timeline |
| `Action_None` | 80 | 112 | 33 | inferred_complete_timeline |
| `Action_None` | 114 | 267 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 88 | 51 | inferred_complete_timeline |
| `Action_None` | 97 | 249 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 396 | 359 | inferred_complete_timeline |
| `Action_None` | 400 | 405 | 6 | inferred_complete_timeline |
| `Action_None` | 423 | 442 | 20 | inferred_complete_timeline |
| `Action_None` | 454 | 479 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 371 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 459 | 78 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 460 | 474 | 15 | inferred_complete_timeline |
| `Action_None` | 475 | 479 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–462
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 108 | 71 | inferred_complete_timeline |
| `Action_None` | 120 | 459 | 340 | inferred_complete_timeline |
| `Action_None` | 461 | 462 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 113 | 76 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 296 | 174 | inferred_complete_timeline |
| `Action_None` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 479 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 99 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 479 | 442 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 56–178 | 93 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 68–119 | 52 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 91–100 | 10 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 120–479 | 360 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 122–439 | 311 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 128–479 | 347 | 7 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 132–479 | 340 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 135–165 | 21 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 137–144 | 7 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 143–381 | 237 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 150–375 | 198 | 9 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 172–400 | 229 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 189–403 | 211 | 4 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 205–209 | 5 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 217–479 | 255 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 252–479 | 228 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 281–406 | 126 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 312–335 | 24 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 319–450 | 81 | 6 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 322–324 | 3 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 327–452 | 30 | 6 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 348–359 | 8 | 3 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 361–371 | 8 | 2 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 361–450 | 69 | 2 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 365–479 | 111 | 4 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 377–380 | 4 | 1 | Undefined position; Undefined team |
| `51` | `78` | Position_Unknown | Team_Unknown | 387–479 | 76 | 6 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 401–403 | 3 | 1 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 404–478 | 30 | 7 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 421–446 | 13 | 4 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 451–479 | 29 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 456–472 | 6 | 2 | Undefined position; Undefined team |
| `57` | `90` | Position_Unknown | Team_Unknown | 469–479 | 11 | 1 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 473–479 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 132 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [38-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-479] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-396] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-405] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-442] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-113] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-296] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-459] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-112] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-267] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-357] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-470] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-371] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-212] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-178] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-385] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-439] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-368] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [370-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-418] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-381] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-310] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-375] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-400] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-403] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-405] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-471] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-406] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-335] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-450] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-423] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-452] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-365] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-383] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-450] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-394] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-404] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-429] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-394] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-423] for track '51' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-421] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-441] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '56' has 1 frames without a visible bounding box.
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