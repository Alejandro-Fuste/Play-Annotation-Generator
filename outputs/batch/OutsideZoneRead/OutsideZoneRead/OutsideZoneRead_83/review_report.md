# Play-Annotation-Generator Annotation Review — OutsideZoneRead_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_83`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 207 | START | 207 | 214 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 217 | START | 217 | 274 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 217 | START | 217 | 221 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `9` | `9` | 222 | START | 224 | 233 |

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
- **Visible Frames:** 0–345
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 224 | 233 | 10 | inferred_complete_timeline |
| `Action_None` | 234 | 345 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PressEdge` | 217 | 274 | 58 | inferred_complete_timeline |
| `Action_None` | 280 | 389 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 389 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 389 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 214 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 217 | 222 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 280 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 315 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 389 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 370 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 312 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 358 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 389 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 342 | 343 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 347 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 389 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 335 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 389 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 313 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 333 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 337 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 6–380 | 324 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 39–377 | 335 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 54–374 | 321 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 58–389 | 314 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 58–389 | 332 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 235–389 | 155 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 257–264 | 8 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 274–280 | 7 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 287–347 | 61 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 290–319 | 25 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 300–314 | 15 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 305–309 | 5 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 316–341 | 14 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 323–328 | 5 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 340–387 | 33 | 5 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 349–351 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `9` (QB): Annotated start 222 != Inferred start 224

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 67 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [217-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-255] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-313] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-333] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [217-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-345] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-367] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-347] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-312] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-358] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-370] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [217-222] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-318] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-380] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-377] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-374] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-264] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-280] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-347] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-309] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-309] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-347] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-367] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-380] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-351] for track '36' has 1 frames without a visible bounding box.
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

</details>