# Play-Annotation-Generator Annotation Review — InsideZoneRead_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_128`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 148
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 7
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 111 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `14` | `13` | 109 | START | 109 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 112 | START | 112 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 112 | START | 112 | 180 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 112 | START | 112 | 185 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `11` | `10` | 120 | END | 109 | 120 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `11` | `10` | 125 | START | 125 | 129 |
| ✅ EXACT | `Action_Handoff` | DE2 | `11` | `10` | 130 | START | 130 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 146 | START | 178 | 282 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 282 | 105 | inferred_complete_timeline |
| `Action_BallCarry` | 285 | 290 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 309 | 335 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 180 | 69 | inferred_complete_timeline |
| `Action_None` | 187 | 257 | 71 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 277 | 292 | 16 | inferred_complete_timeline |
| `Action_None` | 294 | 301 | 8 | inferred_complete_timeline |
| `Action_None` | 328 | 335 | 8 | inferred_complete_timeline |
| `Action_None` | 338 | 348 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 186 | 359 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 186 | 359 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 190 | 82 | inferred_complete_timeline |
| `Action_None` | 193 | 221 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_SnapReceive` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 178 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 108 | 54 | inferred_complete_timeline |
| `Action_None` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 146 | 38 | inferred_complete_timeline |
| `Action_None` | 170 | 218 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 152 | 44 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 194 | 32 | inferred_complete_timeline |
| `Action_None` | 198 | 264 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 152 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–135 | 136 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–329 | 233 | 6 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 2–265 | 178 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 15–245 | 132 | 11 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 136–359 | 149 | 9 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 143–347 | 152 | 7 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 155–233 | 76 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 166–358 | 193 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 180–296 | 84 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 181–265 | 62 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 182–325 | 48 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 200–359 | 136 | 5 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 209–359 | 151 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 211–290 | 65 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 237–346 | 98 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 243–357 | 109 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 262–280 | 8 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 266–273 | 8 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 277–359 | 83 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 280–358 | 79 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 284–296 | 13 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 311–338 | 13 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 320–359 | 28 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 258: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [109-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-264] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [297-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-335] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-257] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-335] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-146] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-38] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-337] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-229] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-262] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-298] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-325] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-294] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-346] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-344] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-358] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>