# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_94

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_94`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 250
- **Validation Warnings:** 319
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 235
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `47` | `36` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `47` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 16 | START | 16 | 70 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 71 | START | 71 | 75 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `47` | `36` | 183 | START | 183 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `47` | `36` | 201 | START | 201 | 373 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_KickBall` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 185 | 110 | inferred_complete_timeline |
| `Action_None` | 187 | 425 | 239 | inferred_complete_timeline |
| `Action_None` | 427 | 599 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–584
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 584 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 599 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–580
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 575 | 560 | inferred_complete_timeline |
| `Action_None` | 577 | 580 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 225 | 210 | inferred_complete_timeline |
| `Action_None` | 229 | 430 | 202 | inferred_complete_timeline |
| `Action_None` | 432 | 599 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 205 | 190 | inferred_complete_timeline |
| `Action_None` | 208 | 599 | 392 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 137 | 122 | inferred_complete_timeline |
| `Action_None` | 140 | 243 | 104 | inferred_complete_timeline |
| `Action_None` | 256 | 424 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–595
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 135 | 120 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 595 | 454 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 327 | 312 | inferred_complete_timeline |
| `Action_None` | 352 | 525 | 174 | inferred_complete_timeline |
| `Action_None` | 527 | 531 | 5 | inferred_complete_timeline |
| `Action_None` | 535 | 599 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 599 | 584 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 369 | 354 | inferred_complete_timeline |
| `Action_None` | 372 | 376 | 5 | inferred_complete_timeline |
| `Action_None` | 378 | 599 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 365 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–391
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 209 | 194 | inferred_complete_timeline |
| `Action_None` | 214 | 316 | 103 | inferred_complete_timeline |
| `Action_None` | 319 | 391 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 94 | 79 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 115 | 100 | inferred_complete_timeline |
| `Action_None` | 118 | 131 | 14 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 243 | 65 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 91 | 333 | 243 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–213 | 183 | 11 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–106 | 95 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–209 | 189 | 11 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–264 | 247 | 13 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 27–72 | 24 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 40–209 | 127 | 20 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 47–217 | 150 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 59–61 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 80–599 | 507 | 8 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 81–422 | 339 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 85–256 | 158 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 90–599 | 487 | 7 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 114–467 | 351 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 121–599 | 477 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 122–164 | 22 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 128–460 | 333 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 136–142 | 7 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 143–149 | 4 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 167–599 | 431 | 5 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 187–193 | 5 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 223–235 | 13 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 244–251 | 8 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 259–477 | 210 | 3 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 315–319 | 5 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 315–330 | 7 | 2 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 332–599 | 268 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 352–430 | 38 | 4 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 359–360 | 2 | 1 | Undefined position; Undefined team |
| `49` | `78` | Position_Unknown | Team_Unknown | 364–471 | 107 | 2 | Undefined position; Undefined team |
| `50` | `83` | Position_Unknown | Team_Unknown | 373–427 | 25 | 5 | Undefined position; Undefined team |
| `51` | `87` | Position_Unknown | Team_Unknown | 381–599 | 211 | 5 | Undefined position; Undefined team |
| `52` | `88` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |
| `53` | `89` | Position_Unknown | Team_Unknown | 384–493 | 72 | 11 | Undefined position; Undefined team |
| `54` | `92` | Position_Unknown | Team_Unknown | 392–443 | 52 | 1 | Undefined position; Undefined team |
| `55` | `93` | Position_Unknown | Team_Unknown | 394–428 | 29 | 5 | Undefined position; Undefined team |
| `56` | `95` | Position_Unknown | Team_Unknown | 403–485 | 75 | 5 | Undefined position; Undefined team |
| `57` | `96` | Position_Unknown | Team_Unknown | 409–460 | 6 | 3 | Undefined position; Undefined team |
| `58` | `97` | Position_Unknown | Team_Unknown | 410–421 | 5 | 2 | Undefined position; Undefined team |
| `59` | `99` | Position_Unknown | Team_Unknown | 419–489 | 30 | 6 | Undefined position; Undefined team |
| `60` | `103` | Position_Unknown | Team_Unknown | 431–432 | 2 | 1 | Undefined position; Undefined team |
| `61` | `104` | Position_Unknown | Team_Unknown | 447–448 | 2 | 1 | Undefined position; Undefined team |
| `62` | `105` | Position_Unknown | Team_Unknown | 461–463 | 3 | 1 | Undefined position; Undefined team |
| `63` | `111` | Position_Unknown | Team_Unknown | 488–490 | 3 | 1 | Undefined position; Undefined team |
| `64` | `119` | Position_Unknown | Team_Unknown | 511–519 | 7 | 2 | Undefined position; Undefined team |
| `65` | `122` | Position_Unknown | Team_Unknown | 569–575 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `47` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 96, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '607,612,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 217 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [16-575] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-580] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-365] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-584] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-424] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-135] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-595] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-599] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-430] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-327] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-525] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-531] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-316] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-391] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-333] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-425] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-243] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-94] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-135] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-73] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-137] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-221] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-241] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-70] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-165] for track '22' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-253] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-599] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-415] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-219] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-219] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-281] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-599] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-467] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-460] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-373] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-599] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-235] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-251] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-301] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-477] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-381] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-468] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-410] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-427] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-392] for track '51' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-412] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-426] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-459] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-493] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-443] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-404] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-424] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-428] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-441] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-460] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-480] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-485] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-450] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-471] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-489] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-575] for track '65' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_94'; source metadata written as null.

</details>