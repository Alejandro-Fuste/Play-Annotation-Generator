# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_120`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 166
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | FB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 40 | START | 40 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 40 | START | 40 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | C | `4` | `4` | 40 | START | 40 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 40 | START | 40 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 40 | START | 40 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | FB | `6` | `6` | 45 | START | 45 | 198 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 157 | START | 157 | 172 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_None` | 173 | 198 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 239 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 248 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 297 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 302 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PressEdge` | 45 | 198 | 154 | inferred_complete_timeline |
| `Action_PressEdge` | 202 | 226 | 25 | inferred_complete_timeline |
| `Action_None` | 227 | 449 | 223 | inferred_complete_timeline |
| `Action_None` | 460 | 461 | 2 | inferred_complete_timeline |
| `Action_None` | 464 | 479 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 198 | 112 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 174 | 88 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 245 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 196 | 110 | inferred_complete_timeline |
| `Action_None` | 198 | 305 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 227 | 141 | inferred_complete_timeline |
| `Action_None` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_None` | 249 | 281 | 33 | inferred_complete_timeline |
| `Action_None` | 291 | 479 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 291 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 323 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 227 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 312 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 160 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 213 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 274 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 183 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 238 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 250 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 269 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 366 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 376 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 249 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 208 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 479 | 268 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 173–226 | 54 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 176–333 | 154 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 177–179 | 3 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 210–327 | 75 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 214–279 | 49 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 222–470 | 241 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 224–231 | 8 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 231–238 | 8 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 245–276 | 32 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 254–317 | 57 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 271–321 | 51 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 283–479 | 196 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 291–378 | 75 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 306–382 | 77 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 319–479 | 139 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 345–451 | 84 | 6 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 347–475 | 122 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 352–479 | 124 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 358–479 | 122 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 372–479 | 106 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 410–479 | 67 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 418–479 | 59 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 424–479 | 55 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 434–479 | 46 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 441–454 | 14 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 453–479 | 27 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 457–479 | 23 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 458–479 | 11 | 3 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 463–474 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 242: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [87-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-291] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-302] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-196] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-305] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-323] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [45-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-227] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-183] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-366] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-376] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-249] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-333] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-327] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-273] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-238] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-470] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-276] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-317] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-316] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-368] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-378] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-382] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-448] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-348] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-412] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-432] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-451] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-459] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-462] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-475] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-404] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-479] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-444] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-436] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-435] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-451] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-454] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-459] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-464] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-474] for track '44' has 1 frames without a visible bounding box.
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

</details>