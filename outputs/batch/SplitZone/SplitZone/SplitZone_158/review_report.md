# Play-Annotation-Generator Annotation Review — SplitZone_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_158`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 1
- **Action Segments:** 103
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 26 | START | 27 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 26 | START | 27 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 26 | START | 27 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 26 | START | 32 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 26 | START | 27 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 26 | START | 27 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 26 | START | 27 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 26 | START | 27 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 26 | START | 27 | 83 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 84 | START | 84 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `16` | 87 | START | 87 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 87 | START | 87 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 87 | START | 87 | 128 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 87 | START | 90 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 87 | START | 87 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `13` | `13` | 89 | END | 85 | 86 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `12` | `12` | 91 | START | 91 | 263 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `5` | `5` | 104 | START | 104 | 263 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `13` | `13` | 112 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `0` | `0` | 120 | START | 120 | 325 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 263 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 57 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_None` | 127 | 344 | 218 | inferred_complete_timeline |
| `Action_None` | 346 | 356 | 11 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 119 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 325 | 206 | inferred_complete_timeline |
| `Action_BallCarry` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 90 | 64 | inferred_complete_timeline |
| `Action_SplitBlock` | 91 | 263 | 173 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 32–354
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 86 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 150 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 263 | 112 | inferred_complete_timeline |
| `Action_None` | 264 | 326 | 63 | inferred_complete_timeline |
| `Action_None` | 328 | 354 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 27–137
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 128 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 104 | 263 | 160 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 126 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 263 | 136 | inferred_complete_timeline |
| `Action_None` | 264 | 324 | 61 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 263 | 177 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 27–356
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 52 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 351 | 266 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 291 | 208 | inferred_complete_timeline |
| `Action_None` | 293 | 338 | 46 | inferred_complete_timeline |
| `Action_None` | 341 | 359 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 27–146
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 146 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 27–164
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 164 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–357
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 259 | 176 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |
| `Action_None` | 276 | 282 | 7 | inferred_complete_timeline |
| `Action_None` | 289 | 344 | 56 | inferred_complete_timeline |
| `Action_None` | 351 | 357 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 27–46 | 11 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 66–359 | 280 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 93–101 | 8 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 108–359 | 240 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 123–359 | 237 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 145–359 | 215 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 153–359 | 207 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 160–252 | 93 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 170–359 | 188 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–359 | 183 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 186–340 | 152 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 195–327 | 69 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 199–209 | 11 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 258–359 | 102 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 263–320 | 39 | 6 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 270–359 | 90 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 322–359 | 14 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 329–334 | 6 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 348–353 | 6 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 355–357 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | 27 | 47 | 9 | 42.9% | 35–46 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 87 != Inferred start 90
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `13` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '5' (C) duration 160 frames exceeds threshold 90 frames [start=104, end=263].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [84–89], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=90.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
- ⚠️ Action 'Action_BallCarry' range [120-325] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-259] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-126] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-146] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-291] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-351] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [85-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-344] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-356] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-320] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-359] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-359] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-252] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-308] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-340] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-277] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>