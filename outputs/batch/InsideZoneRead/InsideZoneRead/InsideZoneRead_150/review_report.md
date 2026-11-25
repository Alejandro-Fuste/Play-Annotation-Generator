# Play-Annotation-Generator Annotation Review — InsideZoneRead_150

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_150`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 10
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | DT2 | defense | `6` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | CB5 | defense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | DT2 | defense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | DE2 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `7` | `6` | 148 | START | 148 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 151 | START | 151 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 151 | START | 151 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 151 | START | 151 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 151 | START | 151 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | C | `21` | `20` | 151 | START | 151 | 233 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `6` | `5` | 163 | END | 148 | 163 |
| ✅ EXACT | `Action_ReadDefender` | DT2 | `6` | `5` | 169 | START | 169 | 180 |
| ✅ EXACT | `Action_BlockSecondLevel` | CB5 | `10` | `9` | 174 | START | 174 | 233 |
| ✅ EXACT | `Action_Handoff` | DT2 | `6` | `5` | 181 | START | 181 | 190 |
| ✅ EXACT | `Action_BallCarry` | DE2 | `4` | `3` | 191 | START | 191 | 340 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 336 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 241 | 94 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 284 | 137 | inferred_complete_timeline |
| `Action_None` | 286 | 359 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 359 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 344 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 312 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 233 | 83 | inferred_complete_timeline |
| `Action_None` | 234 | 273 | 40 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 286 | 359 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 233 | 83 | inferred_complete_timeline |
| `Action_None` | 234 | 359 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 233 | 83 | inferred_complete_timeline |
| `Action_None` | 234 | 359 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 233 | 83 | inferred_complete_timeline |
| `Action_None` | 234 | 270 | 37 | inferred_complete_timeline |
| `Action_None` | 281 | 359 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 233 | 83 | inferred_complete_timeline |
| `Action_None` | 234 | 315 | 82 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 359 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 340 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 232 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_SnapReceive` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_None` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 169 | 180 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 181 | 190 | 10 | inferred_complete_timeline |
| `Action_None` | 191 | 286 | 96 | inferred_complete_timeline |
| `Action_None` | 290 | 359 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 288 | 141 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 270 | 123 | inferred_complete_timeline |
| `Action_None` | 280 | 313 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 286 | 139 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–348
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 348 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BallSnap` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_None` | 164 | 265 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 286 | 139 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 174 | 233 | 60 | inferred_complete_timeline |
| `Action_None` | 234 | 306 | 73 | inferred_complete_timeline |
| `Action_None` | 314 | 353 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 2–5 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 274–359 | 86 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 295–297 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 316–359 | 40 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 321–358 | 30 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 326–359 | 30 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 330–359 | 28 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 342–359 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 38 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [148-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-340] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-348] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-353] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-270] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-313] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-336] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-348] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-345] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-350] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_150'; source metadata written as null.

</details>