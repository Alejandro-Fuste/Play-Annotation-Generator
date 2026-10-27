# Play-Annotation-Generator Annotation Review — Counter_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_138`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Fumble`
- **Result Frame:** 629
- **Player Tracks:** 67
- **Ball Tracks:** 1
- **Action Segments:** 149
- **Validation Warnings:** 219
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 127
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `10` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `11` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 79 | START | 79 | 92 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `16` | `15` | 82 | START | 93 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 82 | START | 82 | 130 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `3` | 82 | START | 82 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `9` | `8` | 82 | START | 82 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 92 | END | 79 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `8` | `7` | 109 | START | 109 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `10` | `9` | 132 | START | 140 | 142 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 92 | 14 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 126 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 234 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 302 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 162 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 188 | 55 | inferred_complete_timeline |
| `Action_None` | 195 | 203 | 9 | inferred_complete_timeline |
| `Action_None` | 207 | 265 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 155 | 77 | inferred_complete_timeline |
| `Action_None` | 164 | 207 | 44 | inferred_complete_timeline |
| `Action_None` | 210 | 221 | 12 | inferred_complete_timeline |
| `Action_None` | 225 | 311 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 92 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 99 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 155 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 82 | 113 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 121 | 130 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 134 | 139 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 151 | 73 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 167 | 89 | inferred_complete_timeline |
| `Action_None` | 175 | 216 | 42 | inferred_complete_timeline |
| `Action_None` | 231 | 286 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 169 | 91 | inferred_complete_timeline |
| `Action_None` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_None` | 193 | 281 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 204 | 126 | inferred_complete_timeline |
| `Action_None` | 210 | 232 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 128 | 50 | inferred_complete_timeline |
| `Action_None` | 130 | 203 | 74 | inferred_complete_timeline |
| `Action_None` | 206 | 443 | 238 | inferred_complete_timeline |
| `Action_None` | 447 | 478 | 32 | inferred_complete_timeline |
| `Action_None` | 491 | 629 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 219 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 137 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–118 | 119 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 33–74 | 8 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 101–107 | 7 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 114–121 | 8 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 117–196 | 68 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 154–306 | 138 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 159–230 | 72 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 176–310 | 134 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 182–622 | 439 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 183–299 | 117 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 192–321 | 130 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 195–221 | 25 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 214–314 | 101 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 234–301 | 62 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 235–453 | 211 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 248–293 | 46 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 255–629 | 336 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 261–337 | 49 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 266–415 | 140 | 3 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 272–296 | 22 | 3 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 356–610 | 241 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 362–629 | 268 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 371–377 | 7 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 381–388 | 8 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 401–424 | 24 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 471–629 | 156 | 3 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 507–510 | 4 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 516–629 | 114 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 517–607 | 57 | 3 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 525–531 | 7 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 533–629 | 97 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 533–629 | 97 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 536–550 | 15 | 1 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 547–575 | 23 | 3 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 551–556 | 5 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 553–629 | 77 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 555–575 | 16 | 2 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 563–564 | 2 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 567–629 | 57 | 2 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 571–592 | 15 | 2 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 574–629 | 54 | 2 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 577–622 | 19 | 3 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 582–617 | 35 | 2 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 589–629 | 41 | 1 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 595–629 | 35 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 602–629 | 28 | 1 | Undefined position; Undefined team |
| `62` | `87` | Position_Unknown | Team_Unknown | 605–629 | 25 | 1 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 605–629 | 25 | 1 | Undefined position; Undefined team |
| `64` | `89` | Position_Unknown | Team_Unknown | 608–629 | 22 | 1 | Undefined position; Undefined team |
| `65` | `90` | Position_Unknown | Team_Unknown | 620–629 | 6 | 2 | Undefined position; Undefined team |
| `66` | `91` | Position_Unknown | Team_Unknown | 627–629 | 3 | 1 | Undefined position; Undefined team |
| `67` | `92` | Position_Unknown | Team_Unknown | 629–629 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | 110 | 110 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `16` (C): Annotated start 82 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 107 frames exceeds threshold 90 frames [start=82, end=188].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [79–92], lower_priority='Action_DownBlock' annotated_start=82, effective_Action_DownBlock_start=93.
- ⚠️ Action 'Action_None' range [79-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-443] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-478] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-286] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-155] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-311] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [109-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [82-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [121-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [134-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-281] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-277] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-294] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-310] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-511] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-601] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-622] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-438] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-453] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-439] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-475] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-626] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-337] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-354] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-400] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-415] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-296] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-594] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-377] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-424] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-583] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-510] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-569] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-607] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-531] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-550] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-564] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-575] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-564] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-585] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-582] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-598] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-622] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-611] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-617] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>