# Play-Annotation-Generator Annotation Review — Power_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_142`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 165
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DT1 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 2 | START | 2 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 2 | START | 6 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 2 | START | 103 | 255 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 2 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 2 | START | 2 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 2 | START | 2 | 419 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `1` | `1` | 227 | START | 227 | 279 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DT1 | `14` | `14` | 227 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `13` | 227 | START | 227 | 240 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 419 | 418 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 6–44
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 26 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 33 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 44 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–385
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 252 | 251 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 385 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 103–255
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 103 | 255 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 226 | 225 | inferred_complete_timeline |
| `Action_PullBlock` | 227 | 240 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 244 | 279 | 36 | inferred_complete_timeline |
| `Action_None` | 280 | 311 | 32 | inferred_complete_timeline |
| `Action_None` | 319 | 350 | 32 | inferred_complete_timeline |
| `Action_None` | 352 | 372 | 21 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 298 | 297 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 368 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–237
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 8 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 203 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 230 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–341
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 255 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 315 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 324 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 341 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–257
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 68 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 257 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–327
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 260 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 327 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 2–402
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 3 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 225 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 259 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 379 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 402 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–252
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 252 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 33 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 341 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 419 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 2–330 | 327 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 2–419 | 389 | 6 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 2–66 | 65 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 2–360 | 337 | 6 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 2–343 | 341 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 95–295 | 196 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 236–261 | 26 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 251–324 | 63 | 5 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 258–371 | 82 | 9 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 260–411 | 129 | 6 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 266–366 | 74 | 7 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 267–419 | 150 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 274–368 | 80 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 282–324 | 43 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 322–418 | 62 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 329–393 | 24 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 330–410 | 79 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 336–341 | 4 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 344–416 | 34 | 5 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 358–379 | 22 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 369–374 | 6 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 374–388 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `14` (DT1)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 286: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 286: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=227, end=115. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [2-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-279] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-338] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-370] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-368] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-297] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-316] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-324] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-343] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-360] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-385] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-341] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-372] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-338] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-315] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-324] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-341] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-327] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-68] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [227-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-372] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-26] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-379] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-402] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-288] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-309] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-324] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-299] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-324] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-330] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-350] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-387] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-397] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-411] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-309] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-321] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-366] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-342] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-324] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-368] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-324] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-369] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-418] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-340] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-393] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-363] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-401] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-413] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-379] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-374] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-388] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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