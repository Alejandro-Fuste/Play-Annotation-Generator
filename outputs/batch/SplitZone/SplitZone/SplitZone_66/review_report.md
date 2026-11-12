# Play-Annotation-Generator Annotation Review — SplitZone_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_66`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 140 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 164 | START | 164 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 167 | START | 167 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 167 | START | 167 | 234 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 167 | START | 179 | 245 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 167 | START | 167 | 239 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 178 | END | 164 | 178 |
| ✅ EXACT | `Action_SplitBlock` | TE | `0` | `0` | 178 | START | 178 | 205 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 185 | START | 185 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 196 | START | 196 | 204 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE | `0` | `0` | 206 | START | 206 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 245 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_SnapReceive` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 185 | 195 | 11 | inferred_complete_timeline |
| `Action_None` | 196 | 277 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 336 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 341 | 342 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_None` | 164 | 176 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 177 | 56 | inferred_complete_timeline |
| `Action_SplitBlock` | 178 | 205 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 206 | 245 | 40 | inferred_complete_timeline |
| `Action_None` | 246 | 307 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 243 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_BallSnap` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 245 | 67 | inferred_complete_timeline |
| `Action_None` | 246 | 351 | 106 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 234 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 245 | 9 | inferred_complete_timeline |
| `Action_None` | 246 | 302 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 237 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–348
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 348 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 208 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 227 | 64 | inferred_complete_timeline |
| `Action_None` | 230 | 255 | 26 | inferred_complete_timeline |
| `Action_None` | 257 | 333 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 227 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 163 | 101 | inferred_complete_timeline |
| `Action_None` | 164 | 199 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 326 | 163 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 242 | 79 | inferred_complete_timeline |
| `Action_None` | 245 | 309 | 65 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_None` | 164 | 359 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–359 | 356 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 45–49 | 5 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 81–86 | 6 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 119–359 | 239 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 154–159 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 155–200 | 19 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 169–172 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 216–294 | 79 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 225–231 | 7 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 231–271 | 39 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 275–300 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 167 != Inferred start 179
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 134: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [164–178], lower_priority='Action_ZoneBlock' annotated_start=167, effective_Action_ZoneBlock_start=179.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-307] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-309] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [341-342] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-351] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-351] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-348] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 164, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [164-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-294] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-265] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-300] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>