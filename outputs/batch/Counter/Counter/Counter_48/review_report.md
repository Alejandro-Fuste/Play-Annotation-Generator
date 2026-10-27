# Play-Annotation-Generator Annotation Review — Counter_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_48`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 30
- **Ball Tracks:** 1
- **Action Segments:** 103
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 193 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 194 | START | 194 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `1` | `0` | 200 | START | 200 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `12` | `11` | 200 | START | 200 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `3` | `2` | 200 | START | 200 | 215 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `11` | `10` | 200 | START | 208 | 209 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `5` | `4` | 200 | START | 200 | 275 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 207 | END | 194 | 207 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 217 | START | 217 | 230 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `2` | `1` | 231 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 275 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_SnapReceive` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 217 | 230 | 14 | inferred_complete_timeline |
| `Action_None` | 231 | 254 | 24 | inferred_complete_timeline |
| `Action_None` | 257 | 272 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 200 | 275 | 76 | inferred_complete_timeline |
| `Action_None` | 276 | 288 | 13 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 315 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 239 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 243 | 275 | 33 | inferred_complete_timeline |
| `Action_None` | 276 | 285 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 325 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–472
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_BallSnap` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 227 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 239 | 248 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 260 | 275 | 16 | inferred_complete_timeline |
| `Action_None` | 276 | 337 | 62 | inferred_complete_timeline |
| `Action_None` | 352 | 465 | 114 | inferred_complete_timeline |
| `Action_None` | 467 | 468 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 472 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 112 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 199 | 74 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 227 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 275 | 46 | inferred_complete_timeline |
| `Action_None` | 276 | 307 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 215 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 217 | 233 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 245 | 257 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 260 | 67 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 342 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 254 | 61 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 269 | 301 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 193 | 105 | inferred_complete_timeline |
| `Action_None` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_None` | 219 | 274 | 56 | inferred_complete_timeline |
| `Action_None` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_None` | 282 | 302 | 21 | inferred_complete_timeline |
| `Action_None` | 306 | 328 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 224 | 304 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 240 | 47 | inferred_complete_timeline |
| `Action_None` | 242 | 264 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 231 | 38 | inferred_complete_timeline |
| `Action_None` | 260 | 273 | 14 | inferred_complete_timeline |
| `Action_None` | 301 | 321 | 21 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 479 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 162–304 | 116 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 270–479 | 189 | 5 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 278–479 | 201 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 284–479 | 196 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 307–479 | 173 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 309–316 | 8 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 358–479 | 121 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 366–369 | 4 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 379–479 | 98 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 395–479 | 85 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 401–479 | 79 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 435–440 | 5 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 440–479 | 40 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `24` | 294 | 315 | 18 | 81.8% | 296, 299, 303, 305 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (6 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=231, end=227. Clamping end to start.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [194–207], lower_priority='Action_PullBlock' annotated_start=200, effective_Action_PullBlock_start=208.
- ⚠️ Action 'Action_DownBlock' range [200-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [200-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [217-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [240-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [245-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-260] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-325] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-274] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-302] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [208-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [216-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [236-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [239-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [252-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-337] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-465] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [200-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-254] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-272] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-304] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-349] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-473] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-373] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-479] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-406] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-471] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-437] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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