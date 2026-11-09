# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_173

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_173`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 148 | START | 148 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 148 | START | 148 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 148 | START | 148 | 177 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `8` | `8` | 148 | START | 171 | 177 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 166 | START | 166 | 177 |

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
- **Visible Frames:** 0–370
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_Handoff` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 214 | 33 | inferred_complete_timeline |
| `Action_None` | 218 | 370 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 268 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 286 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 337 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 249 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 341 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 372 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 388 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 177 | 30 | inferred_complete_timeline |
| `Action_None` | 178 | 217 | 40 | inferred_complete_timeline |
| `Action_None` | 219 | 380 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 290 | 107 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 177 | 30 | inferred_complete_timeline |
| `Action_None` | 178 | 194 | 17 | inferred_complete_timeline |
| `Action_None` | 196 | 215 | 20 | inferred_complete_timeline |
| `Action_None` | 219 | 353 | 135 | inferred_complete_timeline |
| `Action_None` | 360 | 400 | 41 | inferred_complete_timeline |
| `Action_None` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–406
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 177 | 30 | inferred_complete_timeline |
| `Action_None` | 178 | 304 | 127 | inferred_complete_timeline |
| `Action_None` | 319 | 343 | 25 | inferred_complete_timeline |
| `Action_None` | 352 | 367 | 16 | inferred_complete_timeline |
| `Action_None` | 369 | 378 | 10 | inferred_complete_timeline |
| `Action_None` | 385 | 406 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 419 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 176 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 419 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 310 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 326 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 337 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 353 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–298 | 278 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 22–98 | 77 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 141–236 | 88 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 155–169 | 15 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 165–265 | 101 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 190–282 | 83 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 196–419 | 220 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 197–419 | 208 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 208–284 | 76 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 235–419 | 169 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 240–419 | 173 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 273–310 | 37 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 277–419 | 93 | 7 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 288–419 | 131 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 296–419 | 87 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 300–376 | 77 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 311–419 | 86 | 6 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 333–350 | 14 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 369–419 | 51 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 384–419 | 34 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 392–419 | 26 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 395–419 | 22 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 406–419 | 11 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 416–419 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (LG): Annotated start 148 != Inferred start 171

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 348: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-337] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-304] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-367] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-406] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-380] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-214] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-370] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-268] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-286] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-337] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-353] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-400] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-249] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-341] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-372] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-388] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-193] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-267] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-358] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-284] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-340] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-348] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-353] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-306] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-290] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-363] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-393] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-412] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-415] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-308] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-419] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-376] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-332] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-346] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-362] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-339] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-350] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-398] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-397] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-400] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>