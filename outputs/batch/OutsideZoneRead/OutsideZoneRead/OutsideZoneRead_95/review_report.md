# Play-Annotation-Generator Annotation Review — OutsideZoneRead_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_95`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 179
- **Validation Warnings:** 238
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 157
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB1 | defense | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 20 | START | 36 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 20 | START | 36 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 20 | START | 36 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 20 | START | 36 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 20 | START | 36 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 20 | START | 36 | 91 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `1` | `1` | 282 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 282 | START | 282 | 323 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `5` | `5` | 282 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB1 | `11` | `11` | 288 | START | 288 | 305 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `6` | `6` | 292 | START | 292 | 305 |
| ✅ EXACT | `Action_Handoff` | LB1 | `11` | `11` | 306 | START | 306 | 311 |

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
- **Visible Frames:** 36–211
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 111 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 211 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 36–449
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 113 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 230 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 291 | 57 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 306 | 449 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 36–149
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 91 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 149 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 36–449
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 140 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 210 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 253 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 281 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 323 | 42 | inferred_complete_timeline |
| `Action_None` | 324 | 360 | 37 | inferred_complete_timeline |
| `Action_None` | 366 | 386 | 21 | inferred_complete_timeline |
| `Action_None` | 406 | 417 | 12 | inferred_complete_timeline |
| `Action_None` | 422 | 431 | 10 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 36–147
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 147 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 36–232
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 232 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 36–231
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 231 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 36–449
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 114 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 171 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 226 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 449 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 36–449
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 126 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 228 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 259 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 449 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 36–449
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 114 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 186 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 206 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 243 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 265 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 287 | 21 | inferred_complete_timeline |
| `Action_PressEdge` | 288 | 305 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PressEdge` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 449 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 36–134
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 134 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 36–202
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 118 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 162 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 202 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 36–266
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 126 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 249 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 36–279
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 171 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 220 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 267 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 279 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 36–272 | 185 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 70–143 | 74 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 111–127 | 10 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 150–449 | 298 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 156–432 | 251 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 160–177 | 17 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 166–395 | 214 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 189–199 | 10 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 200–241 | 42 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 214–364 | 114 | 7 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 221–449 | 198 | 7 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 227–393 | 86 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 239–449 | 154 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 242–449 | 208 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 243–325 | 70 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 260–304 | 45 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 272–275 | 4 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 281–416 | 124 | 4 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 286–449 | 160 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 303–449 | 123 | 8 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 305–408 | 94 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 308–342 | 30 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 315–358 | 44 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 341–364 | 17 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 355–367 | 13 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 358–449 | 28 | 4 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 358–449 | 76 | 5 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 368–426 | 45 | 6 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 369–443 | 52 | 5 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 388–443 | 40 | 4 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 395–396 | 2 | 1 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 395–431 | 31 | 3 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 396–449 | 41 | 3 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 411–449 | 19 | 2 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 430–443 | 14 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 431–442 | 11 | 2 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 432–449 | 18 | 1 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 434–449 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `5` (RG)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 156 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 192: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '1' has invalid range: start=282, end=232. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '5' has invalid range: start=282, end=147. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [36-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-232] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-231] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [282-323] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-386] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-417] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-431] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-134] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-171] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-279] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-186] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-171] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-126] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-172] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-249] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-118] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-178] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-366] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-432] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-360] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-364] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-375] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-382] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-395] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-241] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-289] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-310] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-355] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-324] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-346] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-374] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-387] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-273] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-302] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-377] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-416] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-449] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-338] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-364] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-380] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-408] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-332] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-342] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-358] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-353] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-364] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-367] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-364] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-362] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-389] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-371] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-376] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-386] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-426] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-379] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-397] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-443] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-396] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-412] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-429] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-443] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-396] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-402] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-422] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-431] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-405] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-425] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-443] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-442] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-440] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>