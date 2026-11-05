# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_57`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 165
- **Validation Warnings:** 204
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `33` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `33` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 2 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `13` | `13` | 3 | START | 3 | 11 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 65 | START | 65 | 75 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `33` | `28` | 194 | START | 194 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `33` | `28` | 202 | START | 202 | 512 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `33` | `28` | 513 | START | 513 | 518 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 73 | 71 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 226 | 224 | inferred_complete_timeline |
| `Action_None` | 230 | 539 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 259 | 257 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 450 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_LongSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_LongSnap` | 13 | 64 | 52 | inferred_complete_timeline |
| `Action_None` | 65 | 539 | 475 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 74 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 539 | 464 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 72 | 70 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 52 | 50 | inferred_complete_timeline |
| `Action_None` | 55 | 539 | 485 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 64 | 34 | inferred_complete_timeline |
| `Action_PuntBall` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_None` | 76 | 230 | 155 | inferred_complete_timeline |
| `Action_None` | 233 | 418 | 186 | inferred_complete_timeline |
| `Action_None` | 420 | 538 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 29 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 131 | 199 | 69 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 260 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 50 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 95 | 93 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 202 | 78 | inferred_complete_timeline |
| `Action_None` | 208 | 539 | 332 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 40 | 539 | 500 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–499
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 125 | 123 | inferred_complete_timeline |
| `Action_None` | 127 | 215 | 89 | inferred_complete_timeline |
| `Action_None` | 218 | 499 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 26 | 24 | inferred_complete_timeline |
| `Action_None` | 32 | 282 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–519
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_None` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_None` | 56 | 85 | 30 | inferred_complete_timeline |
| `Action_None` | 88 | 519 | 432 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 230 | 228 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 246 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–452
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 66 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 264 | 193 | inferred_complete_timeline |
| `Action_None` | 268 | 311 | 44 | inferred_complete_timeline |
| `Action_None` | 314 | 452 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 539 | 537 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–437
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 437 | 435 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–34 | 9 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 53–539 | 487 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 55–539 | 476 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 80–81 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 85–182 | 94 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 93–528 | 431 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 108–110 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 137–233 | 13 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 137–539 | 403 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 147–539 | 385 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 170–173 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 185–199 | 13 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 218–225 | 6 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 249–252 | 4 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 251–539 | 287 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 258–284 | 27 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 292–466 | 175 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 301–539 | 239 | 1 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 343–409 | 31 | 6 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 365–366 | 2 | 1 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 380–384 | 5 | 1 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 385–409 | 18 | 2 | Undefined position; Undefined team |
| `46` | `73` | Position_Unknown | Team_Unknown | 396–514 | 85 | 9 | Undefined position; Undefined team |
| `47` | `74` | Position_Unknown | Team_Unknown | 418–420 | 3 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 436–447 | 11 | 2 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 439–537 | 51 | 11 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 445–539 | 95 | 1 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 450–539 | 89 | 2 | Undefined position; Undefined team |
| `52` | `84` | Position_Unknown | Team_Unknown | 458–474 | 16 | 2 | Undefined position; Undefined team |
| `53` | `85` | Position_Unknown | Team_Unknown | 477–478 | 2 | 1 | Undefined position; Undefined team |
| `54` | `87` | Position_Unknown | Team_Unknown | 507–508 | 2 | 1 | Undefined position; Undefined team |
| `55` | `89` | Position_Unknown | Team_Unknown | 531–533 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `33` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 129 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [3-230] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-437] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-452] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-17] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-38] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-539] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-48] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-260] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-259] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-450] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-418] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-538] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-50] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [3-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [13-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-539] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-226] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-202] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-215] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-499] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-39] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-519] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-539] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-80] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-143] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-175] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-514] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-523] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-259] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-434] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-284] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-466] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-539] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-368] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-393] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-384] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-400] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-411] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-453] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-484] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-496] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-510] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-420] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-442] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-447] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-461] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-528] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-537] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-491] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-470] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>