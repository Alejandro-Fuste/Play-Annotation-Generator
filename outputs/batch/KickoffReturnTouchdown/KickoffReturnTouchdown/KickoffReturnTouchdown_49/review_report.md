# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_49

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_49`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 238
- **Validation Warnings:** 310
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 226
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `37` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `11` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 13 | START | 13 | 91 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 93 | START | 93 | 97 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `37` | `27` | 207 | START | 207 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `27` | 225 | START | 225 | 235 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–565
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 13 | 91 | 79 | inferred_complete_timeline |
| `Action_KickBall` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 110 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 382 | 263 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 395 | 565 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 62 | 50 | inferred_complete_timeline |
| `Action_None` | 77 | 106 | 30 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 190 | 11 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 200 | 207 | 8 | inferred_complete_timeline |
| `Action_None` | 210 | 222 | 13 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 63 | 118 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–557
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_None` | 17 | 133 | 117 | inferred_complete_timeline |
| `Action_None` | 135 | 194 | 60 | inferred_complete_timeline |
| `Action_None` | 196 | 236 | 41 | inferred_complete_timeline |
| `Action_None` | 241 | 557 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–542
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 24 | 12 | inferred_complete_timeline |
| `Action_None` | 26 | 83 | 58 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 126 | 131 | 6 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 448 | 312 | inferred_complete_timeline |
| `Action_None` | 451 | 475 | 25 | inferred_complete_timeline |
| `Action_None` | 479 | 483 | 5 | inferred_complete_timeline |
| `Action_None` | 493 | 495 | 3 | inferred_complete_timeline |
| `Action_None` | 497 | 499 | 3 | inferred_complete_timeline |
| `Action_None` | 501 | 510 | 10 | inferred_complete_timeline |
| `Action_None` | 530 | 542 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_None` | 128 | 241 | 114 | inferred_complete_timeline |
| `Action_None` | 245 | 286 | 42 | inferred_complete_timeline |
| `Action_None` | 288 | 355 | 68 | inferred_complete_timeline |
| `Action_None` | 360 | 569 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 461 | 449 | inferred_complete_timeline |
| `Action_None` | 463 | 569 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 222 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 198 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 207 | 8 | inferred_complete_timeline |
| `Action_None` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |
| `Action_None` | 352 | 402 | 51 | inferred_complete_timeline |
| `Action_None` | 406 | 526 | 121 | inferred_complete_timeline |
| `Action_None` | 528 | 532 | 5 | inferred_complete_timeline |
| `Action_None` | 538 | 539 | 2 | inferred_complete_timeline |
| `Action_None` | 542 | 569 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 113 | 101 | inferred_complete_timeline |
| `Action_None` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 136 | 9 | inferred_complete_timeline |
| `Action_None` | 138 | 197 | 60 | inferred_complete_timeline |
| `Action_None` | 201 | 225 | 25 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 279 | 44 | inferred_complete_timeline |
| `Action_None` | 281 | 343 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 400 | 388 | inferred_complete_timeline |
| `Action_None` | 402 | 406 | 5 | inferred_complete_timeline |
| `Action_None` | 410 | 569 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–400
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 198 | 186 | inferred_complete_timeline |
| `Action_None` | 211 | 223 | 13 | inferred_complete_timeline |
| `Action_None` | 235 | 252 | 18 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 273 | 11 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 300 | 20 | inferred_complete_timeline |
| `Action_None` | 303 | 363 | 61 | inferred_complete_timeline |
| `Action_None` | 368 | 400 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 227 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 94–220 | 116 | 7 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 96–346 | 210 | 15 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 101–187 | 71 | 9 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 128–130 | 3 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 134–136 | 3 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 135–284 | 141 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 138–145 | 8 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 139–236 | 79 | 8 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 158–364 | 198 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 173–223 | 34 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 181–426 | 227 | 10 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 191–499 | 286 | 7 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 201–435 | 209 | 10 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 239–343 | 99 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 239–242 | 4 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 240–444 | 187 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 254–268 | 8 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 254–256 | 3 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 256–364 | 106 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 264–286 | 9 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 267–569 | 294 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 278–288 | 11 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 304–569 | 263 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 308–398 | 67 | 3 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 320–470 | 151 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 355–423 | 61 | 3 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 356–436 | 81 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 358–365 | 8 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 360–569 | 210 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 376–402 | 23 | 2 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 397–569 | 151 | 11 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 401–402 | 2 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 408–545 | 111 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 419–422 | 4 | 1 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 443–444 | 2 | 1 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 446–447 | 2 | 1 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 457–459 | 3 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 459–569 | 110 | 2 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |
| `57` | `82` | Position_Unknown | Team_Unknown | 473–569 | 96 | 2 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 530–569 | 39 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 51, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '581,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 216 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [13-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-402] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-526] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-532] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-461] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-400] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [13-91] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-382] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-565] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-227] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-123] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-241] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-355] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-569] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-300] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-363] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-400] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-106] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-133] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-194] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-236] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-557] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-448] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-475] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-510] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-542] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-198] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-346] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-148] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-271] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-170] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-237] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-364] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-187] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-288] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-426] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-275] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-331] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-499] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-276] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-398] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-435] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-343] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-444] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-311] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-364] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-569] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-371] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-569] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-398] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-470] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-383] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-423] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-436] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-365] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-569] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-402] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-409] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-463] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-507] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-522] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-550] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-558] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-545] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-526] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-569] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-479] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '58' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_49'; source metadata written as null.

</details>