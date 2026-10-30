# Play-Annotation-Generator Annotation Review — FieldGoalBlock_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_71`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 193
- **Validation Warnings:** 223
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 174
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Right_Tackle | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `15` | `15` | 21 | START | 21 | 34 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 43 | START | 43 | 48 |
| ✅ EXACT | `Action_BlockKick` | Right_Tackle | `10` | `10` | 48 | START | 48 | 68 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PlaceBall` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_None` | 54 | 78 | 25 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_KickBall` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_None` | 49 | 165 | 117 | inferred_complete_timeline |
| `Action_None` | 180 | 189 | 10 | inferred_complete_timeline |
| `Action_None` | 192 | 261 | 70 | inferred_complete_timeline |
| `Action_None` | 264 | 271 | 8 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 52 | 148 | 97 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 190 | 36 | inferred_complete_timeline |
| `Action_None` | 192 | 326 | 135 | inferred_complete_timeline |
| `Action_None` | 329 | 332 | 4 | inferred_complete_timeline |
| `Action_None` | 334 | 453 | 120 | inferred_complete_timeline |
| `Action_None` | 455 | 459 | 5 | inferred_complete_timeline |
| `Action_None` | 461 | 463 | 3 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 37 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 185 | 142 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 479 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 79 | 24 | inferred_complete_timeline |
| `Action_None` | 87 | 106 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 415 | 373 | inferred_complete_timeline |
| `Action_None` | 417 | 479 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 221 | 119 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 242 | 273 | 32 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 84 | 404 | 321 | inferred_complete_timeline |
| `Action_None` | 407 | 479 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 69 | 27 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_BlockKick` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_None` | 69 | 479 | 411 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–455
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 188 | 146 | inferred_complete_timeline |
| `Action_None` | 190 | 346 | 157 | inferred_complete_timeline |
| `Action_None` | 348 | 354 | 7 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 365 | 4 | inferred_complete_timeline |
| `Action_None` | 370 | 391 | 22 | inferred_complete_timeline |
| `Action_None` | 409 | 455 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 103 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 188 | 146 | inferred_complete_timeline |
| `Action_None` | 194 | 417 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 42 | 9 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 38 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 441 | 399 | inferred_complete_timeline |
| `Action_None` | 444 | 479 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 73 | 31 | inferred_complete_timeline |
| `Action_None` | 75 | 91 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 39 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 81 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 29 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 459 | 417 | inferred_complete_timeline |
| `Action_None` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 305 | 263 | inferred_complete_timeline |
| `Action_None` | 319 | 326 | 8 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 356 | 8 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 364 | 368 | 5 | inferred_complete_timeline |
| `Action_None` | 381 | 404 | 24 | inferred_complete_timeline |
| `Action_None` | 407 | 422 | 16 | inferred_complete_timeline |
| `Action_None` | 424 | 437 | 14 | inferred_complete_timeline |
| `Action_None` | 440 | 447 | 8 | inferred_complete_timeline |
| `Action_None` | 449 | 479 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 50–479 | 408 | 10 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 53–458 | 393 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 65–90 | 25 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 66–122 | 41 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 71–386 | 311 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 77–80 | 4 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 87–185 | 89 | 4 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 96–395 | 299 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 99–479 | 374 | 5 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 102–185 | 83 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 108–123 | 8 | 2 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 121–321 | 189 | 4 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 133–479 | 340 | 3 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 134–145 | 6 | 3 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 140–281 | 124 | 9 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 146–165 | 15 | 2 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 150–452 | 244 | 6 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 191–278 | 19 | 4 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 203–409 | 178 | 9 | Undefined position; Undefined team |
| `44` | `84` | Position_Unknown | Team_Unknown | 346–347 | 2 | 1 | Undefined position; Undefined team |
| `45` | `92` | Position_Unknown | Team_Unknown | 439–441 | 3 | 1 | Undefined position; Undefined team |
| `46` | `93` | Position_Unknown | Team_Unknown | 450–470 | 13 | 3 | Undefined position; Undefined team |
| `47` | `95` | Position_Unknown | Team_Unknown | 467–468 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 170 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [43-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-271] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-459] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-346] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-354] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-391] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-455] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-415] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-326] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-453] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-459] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-404] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-479] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 43, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [43-46] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-417] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-37] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-78] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-326] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-404] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-422] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-437] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-447] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-42] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-221] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-273] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-441] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-420] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-454] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-479] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-458] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-92] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-162] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-189] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-386] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-153] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-185] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-121] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-395] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-168] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-441] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-456] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-292] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-170] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-189] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-261] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-281] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-158] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-434] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-452] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-326] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-373] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-387] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-409] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-441] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-458] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '47' has 1 frames without a visible bounding box.
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

</details>