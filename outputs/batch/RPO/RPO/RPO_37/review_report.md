# Play-Annotation-Generator Annotation Review — RPO_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_37`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `35` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 226 | START | 226 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 226 | START | 226 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 226 | START | 226 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 226 | START | 226 | 291 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 226 | START | 226 | 285 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 247 | START | 247 | 262 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 263 | START | 263 | 276 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 277 | START | 277 | 291 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 246 | 22 | inferred_complete_timeline |
| `Action_ReadDefender` | 247 | 262 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 263 | 276 | 14 | inferred_complete_timeline |
| `Action_ThrowPass` | 277 | 291 | 15 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |
| `Action_None` | 272 | 309 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 265 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 291 | 66 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 291 | 66 | inferred_complete_timeline |
| `Action_None` | 292 | 308 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 291 | 66 | inferred_complete_timeline |
| `Action_None` | 292 | 315 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 285 | 60 | inferred_complete_timeline |
| `Action_None` | 312 | 320 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 291 | 66 | inferred_complete_timeline |
| `Action_None` | 292 | 326 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 240 | 16 | inferred_complete_timeline |
| `Action_None` | 246 | 263 | 18 | inferred_complete_timeline |
| `Action_None` | 265 | 312 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 241 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 275 | 51 | inferred_complete_timeline |
| `Action_None` | 277 | 283 | 7 | inferred_complete_timeline |
| `Action_None` | 315 | 317 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 289 | 65 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 389 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_None` | 225 | 389 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 10–289 | 85 | 11 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 23–362 | 220 | 16 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 237–309 | 73 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 241–310 | 70 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 267–302 | 36 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 268–355 | 83 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 282–310 | 26 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 312–389 | 78 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 314–389 | 76 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 314–371 | 58 | 1 | Undefined position; Undefined team |
| `24` | `40` | Position_Unknown | Team_Unknown | 317–332 | 10 | 3 | Undefined position; Undefined team |
| `25` | `43` | Position_Unknown | Team_Unknown | 318–389 | 37 | 2 | Undefined position; Undefined team |
| `26` | `44` | Position_Unknown | Team_Unknown | 319–385 | 67 | 1 | Undefined position; Undefined team |
| `27` | `47` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 370–389 | 20 | 1 | Undefined position; Undefined team |
| `29` | `50` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [225-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-283] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-326] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-309] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [226-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-265] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-22] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-203] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-35] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-330] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-355] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-308] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-355] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-305] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-371] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-385] for track '26' has 1 frames without a visible bounding box.
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

</details>