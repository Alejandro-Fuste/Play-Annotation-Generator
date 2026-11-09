# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_76`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 539
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 206
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | LB1 | defense | `5` | `5` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_PressEdge` | LB1 | `5` | `5` | 80 | START | 80 | 126 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `18` | `16` | 90 | START | 199 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 194 | START | 194 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 194 | START | 194 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 194 | START | 194 | 236 |

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
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 11 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 37 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 111 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 147 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 236 | 43 | inferred_complete_timeline |
| `Action_None` | 237 | 280 | 44 | inferred_complete_timeline |
| `Action_None` | 287 | 289 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 360 | 67 | inferred_complete_timeline |
| `Action_None` | 365 | 366 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 233 | 40 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 319 | 40 | inferred_complete_timeline |
| `Action_None` | 321 | 449 | 129 | inferred_complete_timeline |
| `Action_None` | 453 | 539 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_None` | 238 | 292 | 55 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 280 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 295 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 307 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 335 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 539 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 197 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 233 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 273 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PressEdge` | 80 | 126 | 47 | inferred_complete_timeline |
| `Action_None` | 127 | 225 | 99 | inferred_complete_timeline |
| `Action_None` | 243 | 314 | 72 | inferred_complete_timeline |
| `Action_None` | 316 | 321 | 6 | inferred_complete_timeline |
| `Action_None` | 333 | 336 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 517 | 180 | inferred_complete_timeline |
| `Action_None` | 519 | 539 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 284 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 296 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 328 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | Position_Unknown | Team_Unknown | 77–319 | 208 | 8 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 155–229 | 47 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 194–539 | 288 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 199–203 | 5 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 209–288 | 58 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 223–443 | 196 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 224–273 | 45 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 233–321 | 50 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 233–298 | 60 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 243–251 | 9 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 246–539 | 277 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 260–539 | 236 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 264–539 | 271 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 265–506 | 201 | 9 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 271–338 | 68 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 272–539 | 268 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 284–422 | 53 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 291–539 | 249 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 293–539 | 246 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 305–307 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 332–539 | 208 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 358–539 | 165 | 4 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 370–539 | 157 | 4 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 374–539 | 151 | 3 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 376–515 | 132 | 4 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 378–539 | 162 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 386–467 | 76 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 402–539 | 133 | 2 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 424–429 | 5 | 2 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 431–493 | 54 | 3 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 434–490 | 52 | 2 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 436–452 | 17 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 468–487 | 20 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 478–482 | 5 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 498–500 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_Handoff` for actor_track_id `18` (Position_Unknown): Annotated start 90 != Inferred start 199

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 131 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 154: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '16' has invalid range: start=199, end=107. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-296] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-328] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-295] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-335] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-314] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-517] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-539] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-319] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-449] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-197] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-111] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-147] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-292] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-233] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-113] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-196] for track '13' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-424] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-490] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-537] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-443] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-279] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-321] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-292] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-307] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-425] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-433] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-437] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-539] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-355] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-367] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-437] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-506] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-338] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-331] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-422] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-539] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-313] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-464] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-472] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-469] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-482] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-496] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-539] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-507] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [513-525] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-539] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-382] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-474] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-477] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-515] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-539] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-404] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-467] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-426] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-473] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-482] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-493] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-482] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-490] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-452] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-487] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-482] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-500] for track '48' has 1 frames without a visible bounding box.
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

</details>