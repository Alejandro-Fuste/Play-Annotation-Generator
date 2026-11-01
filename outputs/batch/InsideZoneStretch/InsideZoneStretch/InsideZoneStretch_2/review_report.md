# Play-Annotation-Generator Annotation Review — InsideZoneStretch_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneStretch_2`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_PressGap` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 175 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `14` | `14` | 147 | START | 147 | 154 |
| ✅ EXACT | `Action_SnapReceive` | C | `10` | `10` | 154 | END | 147 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 160 | START | 160 | 173 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 160 | START | 160 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 160 | START | 160 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `6` | 160 | START | 160 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 160 | START | 160 | 204 |
| ✅ EXACT | `Action_PressGap` | RB | `8` | `8` | 176 | START | 176 | 190 |
| ✅ EXACT | `Action_Handoff` | C | `10` | `10` | 189 | START | 189 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 203 | START | 203 | 310 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PressGap` | 176 | 190 | 15 | inferred_complete_timeline |
| `Action_None` | 191 | 202 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 310 | 108 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 318 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 321 | 323 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 213–341
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 213 | 293 | 81 | inferred_complete_timeline |
| `Action_None` | 295 | 341 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 204 | 45 | inferred_complete_timeline |
| `Action_None` | 205 | 240 | 36 | inferred_complete_timeline |
| `Action_None` | 243 | 263 | 21 | inferred_complete_timeline |
| `Action_None` | 266 | 389 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 204 | 45 | inferred_complete_timeline |
| `Action_None` | 205 | 233 | 29 | inferred_complete_timeline |
| `Action_None` | 237 | 380 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_SnapReceive` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 173 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 188 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 389 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 204 | 45 | inferred_complete_timeline |
| `Action_None` | 205 | 375 | 171 | inferred_complete_timeline |
| `Action_None` | 377 | 379 | 3 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–385
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 204 | 45 | inferred_complete_timeline |
| `Action_None` | 205 | 385 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 174 | 28 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 189 | 221 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 168 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 174 | 28 | inferred_complete_timeline |
| `Action_None` | 183 | 204 | 22 | inferred_complete_timeline |
| `Action_None` | 206 | 225 | 20 | inferred_complete_timeline |
| `Action_None` | 228 | 297 | 70 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_BallSnap` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 155 | 163 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 215 | 69 | inferred_complete_timeline |
| `Action_None` | 217 | 389 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 276 | 130 | inferred_complete_timeline |
| `Action_None` | 278 | 346 | 69 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 185 | 39 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_None` | 213 | 317 | 105 | inferred_complete_timeline |
| `Action_None` | 330 | 389 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_None` | 147 | 246 | 100 | inferred_complete_timeline |
| `Action_None` | 250 | 280 | 31 | inferred_complete_timeline |
| `Action_None` | 282 | 317 | 36 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–383 | 384 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–365 | 363 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 47–389 | 284 | 10 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 188–212 | 14 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 202–389 | 188 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 206–284 | 78 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 210–304 | 81 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 225–389 | 121 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 249–389 | 140 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 253–389 | 129 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 262–389 | 128 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 294–389 | 77 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 336–382 | 34 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 5: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [147-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-383] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-336] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-365] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-375] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-385] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-318] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-280] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-317] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-346] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-168] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-380] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-297] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-77] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-124] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-226] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-389] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-277] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-273] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-341] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-262] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-360] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-360] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>