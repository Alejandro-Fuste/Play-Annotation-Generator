# Play-Annotation-Generator Annotation Review — SplitZone_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_36`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `17` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 20 | START | 20 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 20 | START | 47 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 20 | START | 20 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 20 | START | 20 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 20 | START | 20 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 20 | START | 20 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `9` | `9` | 193 | START | 193 | 200 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `17` | `13` | 196 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 196 | START | 196 | 274 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `9` | 196 | START | 210 | 216 |
| ✅ EXACT | `Action_SplitBlock` | TE | `11` | `11` | 204 | START | 204 | 253 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `7` | `7` | 209 | END | 194 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `9` | `9` | 217 | START | 217 | 218 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 217 | START | 217 | 234 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 284 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `6` | 294 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–234
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 82 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 139 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 157 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 217 | 234 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–139
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 139 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 20–253
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 203 | 184 | inferred_complete_timeline |
| `Action_SplitBlock` | 204 | 253 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 50 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 192 | 140 | inferred_complete_timeline |
| `Action_BallSnap` | 193 | 200 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 222 | 237 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 243 | 284 | 42 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |
| `Action_None` | 333 | 449 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 47–114
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 114 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–380
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 195 | 176 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 274 | 79 | inferred_complete_timeline |
| `Action_None` | 288 | 380 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 309 | 117 | inferred_complete_timeline |
| `Action_None` | 311 | 343 | 33 | inferred_complete_timeline |
| `Action_None` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_None` | 362 | 366 | 5 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 387 | 13 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 20–444
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 273 | 81 | inferred_complete_timeline |
| `Action_None` | 276 | 395 | 120 | inferred_complete_timeline |
| `Action_None` | 441 | 444 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_None` | 218 | 225 | 8 | inferred_complete_timeline |
| `Action_None` | 229 | 251 | 23 | inferred_complete_timeline |
| `Action_None` | 266 | 276 | 11 | inferred_complete_timeline |
| `Action_None` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 396 | 79 | inferred_complete_timeline |
| `Action_None` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–361
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 250 | 58 | inferred_complete_timeline |
| `Action_None` | 277 | 298 | 22 | inferred_complete_timeline |
| `Action_None` | 301 | 361 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–308
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 277 | 85 | inferred_complete_timeline |
| `Action_None` | 290 | 296 | 7 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–446
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 335 | 143 | inferred_complete_timeline |
| `Action_None` | 338 | 446 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–289
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 193 | 289 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | Position_Unknown | Team_Unknown | 32–39 | 8 | 1 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 63–66 | 4 | 1 | Undefined position; Undefined team |
| `15` | `23` | Position_Unknown | Team_Unknown | 138–153 | 14 | 2 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 146–161 | 16 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 210–449 | 173 | 7 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 211–371 | 101 | 3 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 226–291 | 65 | 2 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 228–257 | 16 | 3 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 245–449 | 119 | 6 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 261–426 | 150 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 262–321 | 41 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 262–449 | 130 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 267–361 | 63 | 6 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 270–286 | 17 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 301–449 | 149 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 307–449 | 143 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 308–449 | 141 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 313–449 | 129 | 5 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 319–449 | 128 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 328–415 | 87 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 330–443 | 112 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 346–449 | 91 | 5 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 355–449 | 95 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 375–396 | 19 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 376–449 | 74 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 386–449 | 64 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 390–449 | 60 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 445–449 | 5 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (RG)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 196 != Inferred start 210
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=294, end=139. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [193–209], lower_priority='Action_ZoneBlock' annotated_start=196, effective_Action_ZoneBlock_start=210.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=196, end=114. Clamping end to start.
- ⚠️ Action 'Action_None' range [193-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-395] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-343] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-335] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-446] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-380] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [194-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [217-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-361] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-50] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [193-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [202-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [217-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [222-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-251] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-396] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' for track '11' starts at frame 204, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SplitBlock' range [204-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-114] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-153] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-449] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-371] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-338] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-400] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-325] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-355] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-446] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-369] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-382] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-391] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-396] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-415] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-398] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-443] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-362] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-395] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-389] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-449] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>