# Play-Annotation-Generator Annotation Review — SplitZone_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_64`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `6` | 43 | START | 43 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 48 | START | 48 | 103 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `6` | `6` | 48 | START | 61 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 48 | START | 48 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 48 | START | 48 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 48 | START | 48 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `12` | `12` | 49 | START | 49 | 57 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 60 | END | 43 | 60 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 77 | START | 77 | 80 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `10` | 81 | START | 81 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_None` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 207 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SplitBlock` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 113 | 127 | 15 | inferred_complete_timeline |
| `Action_None` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 373 | 232 | inferred_complete_timeline |
| `Action_None` | 377 | 387 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 127 | 80 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 127 | 80 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_None` | 140 | 379 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 127 | 67 | inferred_complete_timeline |
| `Action_None` | 128 | 238 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 127 | 80 | inferred_complete_timeline |
| `Action_None` | 128 | 352 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 103 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 112 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 211 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 389 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 214 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 389 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 110 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 389 | 347 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 23–389 | 356 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 57–251 | 130 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 65–389 | 325 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 94–170 | 74 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 114–389 | 275 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 135–389 | 255 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 144–146 | 3 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 144–389 | 245 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 151–389 | 238 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 195–203 | 5 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 202–389 | 188 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 206–389 | 182 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 243–249 | 7 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 248–288 | 20 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 250–314 | 16 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 266–285 | 7 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 274–357 | 40 | 6 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 276–294 | 18 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 277–389 | 113 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 281–356 | 40 | 5 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 284–290 | 7 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 284–296 | 8 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 285–314 | 9 | 3 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 287–362 | 76 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 293–389 | 97 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 302–309 | 7 | 2 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 307–389 | 83 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 310–312 | 3 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 314–347 | 6 | 2 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 327–351 | 25 | 1 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 345–347 | 3 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 352–389 | 38 | 1 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 353–364 | 10 | 2 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 355–375 | 9 | 2 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 357–370 | 11 | 3 | Undefined position; Undefined team |
| `58` | `83` | Position_Unknown | Team_Unknown | 364–386 | 22 | 2 | Undefined position; Undefined team |
| `59` | `84` | Position_Unknown | Team_Unknown | 364–375 | 7 | 2 | Undefined position; Undefined team |
| `60` | `85` | Position_Unknown | Team_Unknown | 365–384 | 15 | 3 | Undefined position; Undefined team |
| `61` | `86` | Position_Unknown | Team_Unknown | 365–372 | 8 | 1 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 369–378 | 10 | 1 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 370–380 | 11 | 1 | Undefined position; Undefined team |
| `64` | `93` | Position_Unknown | Team_Unknown | 374–375 | 2 | 1 | Undefined position; Undefined team |
| `65` | `94` | Position_Unknown | Team_Unknown | 374–378 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `6` (C): Annotated start 48 != Inferred start 61
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [43–60], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=61.
- ⚠️ Action 'Action_None' range [43-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-103] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-112] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-379] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [49-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [101-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [106-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [113-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-373] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-387] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-214] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-99] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-166] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-389] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-347] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-305] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-294] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-362] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-389] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-351] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-389] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-360] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-378] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-375] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-372] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-380] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '65' has 1 frames without a visible bounding box.
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

</details>