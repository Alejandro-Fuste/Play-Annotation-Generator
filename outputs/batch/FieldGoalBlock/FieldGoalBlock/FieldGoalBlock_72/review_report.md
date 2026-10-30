# Play-Annotation-Generator Annotation Review — FieldGoalBlock_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_72`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 70
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 242
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 151
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_BlockKick` | Position_Unknown | Team_Unknown | `30` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 5 | START | 5 | 16 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 26 | START | 26 | 31 |
| ⚠️ START CHANGED | `Action_BlockKick` | Position_Unknown | `30` | `23` | 31 | START | 32 | 36 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PlaceBall` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_None` | 17 | 149 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_KickBall` | 26 | 31 | 6 | inferred_complete_timeline |
| `Action_None` | 32 | 142 | 111 | inferred_complete_timeline |
| `Action_None` | 144 | 479 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 14 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 25 | 10 | inferred_complete_timeline |
| `Action_None` | 26 | 38 | 13 | inferred_complete_timeline |
| `Action_None` | 42 | 58 | 17 | inferred_complete_timeline |
| `Action_None` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 479 | 373 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 370 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 45 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 132 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–442
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 442 | 417 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_None` | 49 | 114 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 51 | 26 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 65 | 40 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 479 | 398 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 61 | 36 | inferred_complete_timeline |
| `Action_None` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 479 | 384 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 33 | 8 | inferred_complete_timeline |
| `Action_None` | 38 | 43 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_None` | 26 | 55 | 30 | inferred_complete_timeline |
| `Action_None` | 57 | 65 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_None` | 26 | 52 | 27 | inferred_complete_timeline |
| `Action_None` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_None` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_None` | 92 | 112 | 21 | inferred_complete_timeline |
| `Action_None` | 115 | 479 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 128 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 479 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 479 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–177 | 172 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–479 | 480 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 7–8 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 32–258 | 179 | 3 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 34–127 | 74 | 4 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 62–301 | 239 | 2 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 67–308 | 241 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 67–357 | 291 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 73–82 | 9 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 79–82 | 4 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 87–291 | 202 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 87–307 | 220 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 108–113 | 6 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 113–303 | 156 | 6 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 116–308 | 189 | 4 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 127–144 | 5 | 2 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 130–132 | 3 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 131–479 | 344 | 2 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 138–142 | 5 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 141–151 | 10 | 2 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 145–282 | 104 | 5 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 162–166 | 4 | 2 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 167–479 | 313 | 1 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 177–303 | 127 | 1 | Undefined position; Undefined team |
| `47` | `78` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `49` | `82` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 250–257 | 7 | 2 | Undefined position; Undefined team |
| `51` | `91` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `52` | `92` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `53` | `95` | Position_Unknown | Team_Unknown | 329–413 | 85 | 1 | Undefined position; Undefined team |
| `54` | `99` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `55` | `100` | Position_Unknown | Team_Unknown | 356–440 | 11 | 4 | Undefined position; Undefined team |
| `56` | `101` | Position_Unknown | Team_Unknown | 377–379 | 3 | 1 | Undefined position; Undefined team |
| `57` | `102` | Position_Unknown | Team_Unknown | 395–399 | 5 | 1 | Undefined position; Undefined team |
| `58` | `103` | Position_Unknown | Team_Unknown | 402–403 | 2 | 1 | Undefined position; Undefined team |
| `59` | `104` | Position_Unknown | Team_Unknown | 407–408 | 2 | 1 | Undefined position; Undefined team |
| `60` | `106` | Position_Unknown | Team_Unknown | 416–418 | 3 | 1 | Undefined position; Undefined team |
| `61` | `107` | Position_Unknown | Team_Unknown | 423–430 | 7 | 2 | Undefined position; Undefined team |
| `62` | `109` | Position_Unknown | Team_Unknown | 429–443 | 14 | 2 | Undefined position; Undefined team |
| `63` | `110` | Position_Unknown | Team_Unknown | 432–455 | 19 | 2 | Undefined position; Undefined team |
| `64` | `114` | Position_Unknown | Team_Unknown | 434–452 | 14 | 2 | Undefined position; Undefined team |
| `65` | `116` | Position_Unknown | Team_Unknown | 435–440 | 6 | 1 | Undefined position; Undefined team |
| `66` | `120` | Position_Unknown | Team_Unknown | 438–442 | 5 | 1 | Undefined position; Undefined team |
| `67` | `121` | Position_Unknown | Team_Unknown | 440–443 | 4 | 1 | Undefined position; Undefined team |
| `68` | `128` | Position_Unknown | Team_Unknown | 459–460 | 2 | 1 | Undefined position; Undefined team |
| `69` | `130` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockKick` for actor_track_id `30` (Position_Unknown): Annotated start 31 != Inferred start 32

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_End` position mapped to `offense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 140 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 146: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [26-53] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-132] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-479] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-53] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-370] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-479] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-479] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-442] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-45] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-64] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-86] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-112] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-479] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-58] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-80] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-479] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [32-36] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-258] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-70] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-105] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-298] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-308] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-284] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-307] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-145] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-245] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-308] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-247] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-167] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-226] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-282] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-303] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-413] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-443] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-442] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-455] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-440] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>