# Play-Annotation-Generator Annotation Review — SplitZone_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_110`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | RB2 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 2 | START | 3 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 2 | START | 3 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 2 | START | 3 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 2 | START | 3 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 2 | START | 3 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `6` | `Group` | 2 | START | 3 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 2 | START | 3 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 2 | START | 3 | 187 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 188 | START | 188 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 191 | START | 191 | 225 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 191 | START | 191 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 191 | START | 191 | 267 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 191 | START | 191 | 254 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `9` | 191 | START | 204 | 267 |
| ✅ EXACT | `Action_SplitBlock` | RB2 | `6` | `6` | 198 | START | 198 | 267 |
| ✅ EXACT | `Action_SnapReceive` | QB | `0` | `0` | 203 | END | 188 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `0` | `0` | 222 | START | 222 | 407 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 267 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_SnapReceive` | 188 | 203 | 16 | inferred_complete_timeline |
| `Action_None` | 204 | 221 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 407 | 186 | inferred_complete_timeline |
| `Action_BallCarry` | 411 | 417 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 227 | 40 | inferred_complete_timeline |
| `Action_None` | 230 | 267 | 38 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 286 | 9 | inferred_complete_timeline |
| `Action_None` | 298 | 388 | 91 | inferred_complete_timeline |
| `Action_None` | 390 | 408 | 19 | inferred_complete_timeline |
| `Action_None` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 197 | 195 | inferred_complete_timeline |
| `Action_SplitBlock` | 198 | 267 | 70 | inferred_complete_timeline |
| `Action_None` | 268 | 384 | 117 | inferred_complete_timeline |
| `Action_None` | 386 | 419 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–226
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 190 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 226 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–295
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 190 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 267 | 77 | inferred_complete_timeline |
| `Action_None` | 268 | 290 | 23 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_BallSnap` | 188 | 203 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 267 | 64 | inferred_complete_timeline |
| `Action_None` | 268 | 318 | 51 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–254
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 190 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 254 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–289
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 190 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 225 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 267 | 38 | inferred_complete_timeline |
| `Action_None` | 268 | 271 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 289 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–315
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 208 | 21 | inferred_complete_timeline |
| `Action_None` | 227 | 315 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 187 | 178 | inferred_complete_timeline |
| `Action_None` | 188 | 419 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–194
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–264
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 187 | 171 | inferred_complete_timeline |
| `Action_None` | 188 | 264 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 419 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–406
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 316 | 129 | inferred_complete_timeline |
| `Action_None` | 321 | 341 | 21 | inferred_complete_timeline |
| `Action_None` | 344 | 388 | 45 | inferred_complete_timeline |
| `Action_None` | 390 | 406 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–283
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 283 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–306
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 188 | 306 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 3–419 | 403 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–419 | 351 | 8 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 219–230 | 9 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 248–304 | 57 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 249–419 | 141 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 257–270 | 14 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 281–419 | 102 | 9 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 283–419 | 137 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 288–419 | 131 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 295–312 | 11 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 298–419 | 122 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 298–406 | 109 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 302–304 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 305–419 | 108 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 325–419 | 73 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 326–370 | 43 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 344–360 | 13 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 378–385 | 8 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 384–390 | 7 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 391–410 | 14 | 2 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 191 != Inferred start 204
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [188–203], lower_priority='Action_ZoneBlock' annotated_start=191, effective_Action_ZoneBlock_start=204.
- ⚠️ Action 'Action_BallCarry' range [222-407] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [411-417] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-419] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-388] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [198-267] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-384] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-316] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-341] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-388] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-406] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-315] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-289] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-304] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-341] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-361] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-407] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-270] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-413] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-406] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-382] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-382] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-405] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-363] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-385] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-401] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-419] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>