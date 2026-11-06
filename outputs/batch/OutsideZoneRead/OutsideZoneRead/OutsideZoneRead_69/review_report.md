# Play-Annotation-Generator Annotation Review — OutsideZoneRead_69

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_69`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 170
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `1` | `1` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 401 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `18` | `Group` | 0 | START | 68 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `1` | `1` | 204 | START | 204 | 206 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 204 | START | 204 | 216 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 217 | START | 217 | 232 |

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
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 204 | 216 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 217 | 232 | 16 | inferred_complete_timeline |
| `Action_None` | 233 | 419 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PressEdge` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_PressEdge` | 208 | 237 | 30 | inferred_complete_timeline |
| `Action_None` | 242 | 311 | 70 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 336 | 5 | inferred_complete_timeline |
| `Action_None` | 339 | 419 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 68–243
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 107 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 243 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 419 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 401 | 402 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 412 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 197 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 276 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 419 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 110 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 128 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 258 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 276 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 287 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 36 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 83 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 251 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 276 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 419 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 403 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 410 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 419 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 376 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 304 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 315 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–279 | 239 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 68–203 | 134 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 68–211 | 136 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 70–109 | 40 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 70–235 | 53 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 75–83 | 9 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 230–252 | 23 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 230–315 | 80 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 230–249 | 13 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 230–419 | 151 | 7 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 247–276 | 25 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 271–419 | 144 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 272–276 | 5 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 285–419 | 81 | 7 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 289–419 | 110 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 302–419 | 97 | 6 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 314–419 | 105 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 314–419 | 106 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 314–419 | 103 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 333–419 | 84 | 3 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 334–419 | 86 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 350–419 | 70 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 351–419 | 54 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'OL' for action 'Action_ZoneBlock' at frame 199 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 119 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-401] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-412] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [204-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [208-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-409] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-376] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-304] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-403] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-410] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-251] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-276] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-276] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-107] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-195] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-309] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-278] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-371] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-394] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-300] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-362] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-375] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-408] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-339] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-419] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-360] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-368] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-337] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-370] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-419] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-370] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>