# Play-Annotation-Generator Annotation Review — WRSlowScreens_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_24`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 104
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `23` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 2 | START | 2 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `1` | `1` | 5 | START | 5 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `12` | 5 | START | 5 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 5 | START | 18 | 317 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 5 | START | 5 | 363 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 5 | START | 5 | 87 |
| ✅ EXACT | `Action_SnapReceive` | RB | `4` | `4` | 17 | END | 2 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | RT | `8` | `8` | 88 | START | 88 | 232 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `2` | `2` | 92 | START | 92 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | `23` | `22` | 136 | START | 136 | 238 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_None` | 104 | 136 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_None` | 18 | 91 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 114 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 308 | 307 | inferred_complete_timeline |
| `Action_None` | 312 | 368 | 57 | inferred_complete_timeline |
| `Action_None` | 389 | 419 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 363 | 359 | inferred_complete_timeline |
| `Action_PassBlock` | 385 | 386 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 228 | 224 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 267 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 274 | 300 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 303 | 330 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 345 | 419 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 317 | 300 | inferred_complete_timeline |
| `Action_PassBlock` | 321 | 374 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 384 | 387 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 62 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 234 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 87 | 83 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 88 | 232 | 145 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 246 | 346 | 101 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 377 | 382 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 44 | 43 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 23 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 14 | 13 | inferred_complete_timeline |
| `Action_None` | 17 | 36 | 20 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 419 | 361 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 218 | 217 | inferred_complete_timeline |
| `Action_None` | 220 | 242 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 159 | 158 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_None` | 189 | 228 | 40 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 33 | 32 | inferred_complete_timeline |
| `Action_None` | 54 | 66 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 44 | 43 | inferred_complete_timeline |
| `Action_None` | 49 | 152 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 66 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 42 | 41 | inferred_complete_timeline |
| `Action_None` | 49 | 89 | 41 | inferred_complete_timeline |
| `Action_None` | 91 | 107 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 35–120 | 60 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 71–265 | 195 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 73–108 | 30 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 122–290 | 151 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 125–385 | 211 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 150–243 | 91 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 183–250 | 16 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 235–419 | 180 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 244–308 | 65 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 282–314 | 30 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 290–419 | 130 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 344–419 | 76 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 360–419 | 60 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 374–375 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 385–419 | 12 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 392–419 | 27 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | 77 | 77 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReleaseToScreen` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `23` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [2-308] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-368] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-42] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-89] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-363] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [385-386] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-23] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [88-232] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [246-346] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [377-382] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-159] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-218] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-242] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-228] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [274-300] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [303-330] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-317] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [321-374] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [384-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-16] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-265] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [136-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [242-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [264-290] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-268] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-341] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-352] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-218] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-308] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-295] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-314] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-415] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>