# Play-Annotation-Generator Annotation Review — Power_288

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_288`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | TE1 | offense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 3 | START | 3 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 3 | START | 3 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 3 | START | 3 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 3 | START | 3 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 3 | START | 3 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 3 | START | 3 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 3 | START | 3 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 3 | START | 3 | 308 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 3 | START | 3 | 376 |
| ✅ EXACT | `Action_DownBlock` | TE1 | `12` | `12` | 247 | START | 247 | 291 |
| ✅ EXACT | `Action_DownBlock` | RT | `14` | `14` | 247 | START | 247 | 291 |
| ✅ EXACT | `Action_DownBlock` | QB | `15` | `15` | 247 | START | 247 | 291 |
| ✅ EXACT | `Action_DownBlock` | RG | `2` | `2` | 247 | START | 247 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `10` | 247 | START | 247 | 264 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 124 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 166 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 246 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 291 | 45 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–376
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 376 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 246 | 244 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 291 | 45 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–324
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 318 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–376
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 308 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 357 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 376 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 246 | 244 | inferred_complete_timeline |
| `Action_PullBlock` | 247 | 264 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 273 | 291 | 19 | inferred_complete_timeline |
| `Action_None` | 292 | 297 | 6 | inferred_complete_timeline |
| `Action_None` | 308 | 314 | 7 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 334 | 12 | inferred_complete_timeline |
| `Action_None` | 337 | 340 | 4 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–348
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 172 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 348 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 246 | 244 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 291 | 45 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 246 | 244 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 291 | 45 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 389 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–275
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 252 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 275 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–337
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 287 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 303 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 337 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 241 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 261 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 268 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 342 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 374 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–321
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 285 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 321 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 389 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 389 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–261
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 261 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–315
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `21` | Position_Unknown | Team_Unknown | 230–235 | 6 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 240–285 | 46 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 277–389 | 113 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 289–295 | 7 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 290–389 | 96 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 290–305 | 16 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 290–389 | 65 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 303–389 | 79 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 305–308 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 314–389 | 74 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 324–332 | 9 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 332–388 | 56 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 333–389 | 53 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 337–389 | 53 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 339–342 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 362–389 | 28 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 373–389 | 17 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 378–389 | 12 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-252] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-275] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-389] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-376] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-321] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-376] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-342] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-374] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [247-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-334] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-124] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-166] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-291] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-79] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-96] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-172] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-185] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-348] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-285] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-295] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-369] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-305] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-293] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-308] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-363] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-332] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-382] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-338] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '37' has 1 frames without a visible bounding box.
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