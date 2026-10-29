# Play-Annotation-Generator Annotation Review — Duo_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_22`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `12` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 322 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 328 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE | `1` | `1` | 223 | START | 223 | 270 |
| ✅ EXACT | `Action_ComboBlock` | LT | `10` | `10` | 223 | START | 223 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `21` | `18` | 223 | START | 223 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `4` | `4` | 223 | START | 223 | 237 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LG | `4` | `4` | 248 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 289 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 326 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 328 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ComboBlock` | 223 | 270 | 48 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 289 | 15 | inferred_complete_timeline |
| `Action_None` | 290 | 328 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ComboBlock` | 223 | 289 | 67 | inferred_complete_timeline |
| `Action_None` | 290 | 290 | 1 | inferred_complete_timeline |
| `Action_None` | 293 | 308 | 16 | inferred_complete_timeline |
| `Action_None` | 312 | 328 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ComboBlock` | 223 | 237 | 15 | inferred_complete_timeline |
| `Action_ComboBlock` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 244 | 245 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 80 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 322 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 328 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 220 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 328 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 59 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 145 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 191 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 296 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 326 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 328 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 65–68 | 4 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 73–312 | 152 | 14 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 87–121 | 35 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 237–290 | 43 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 257–311 | 53 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 265–328 | 64 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 267–307 | 38 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 289–328 | 34 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 292–295 | 4 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 301–328 | 28 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 308–328 | 21 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 326–328 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `4` (3 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `4` (LG)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '4' has invalid range: start=248, end=245. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [223-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-326] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [223-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [239-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [244-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-322] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [223-289] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 290, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [290-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-308] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-328] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-145] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-326] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-80] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [223-268] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-285] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-304] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-121] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-290] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-307] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '26' has 1 frames without a visible bounding box.
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

</details>