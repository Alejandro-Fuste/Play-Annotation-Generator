# Play-Annotation-Generator Annotation Review — Counter_189

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_189`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `25` | `23` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_PlaySideFakeStep` | SAF | defense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 192 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 193 | START | 193 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 195 | START | 195 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 195 | START | 235 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `25` | `23` | 195 | START | 195 | 219 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | `24` | `22` | 195 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | `6` | `5` | 195 | START | 195 | 233 |
| ✅ EXACT | `Action_PlaySideFakeStep` | SAF | `8` | `7` | 200 | START | 200 | 230 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `18` | `17` | 203 | END | 193 | 200 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `18` | `17` | 220 | START | 220 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF | `8` | `7` | 231 | START | 231 | 247 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 263 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 308 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 195 | 233 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 247 | 259 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 264 | 293 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 225 | 33 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |
| `Action_None` | 243 | 248 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 207 | 15 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 331 | 86 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 298 | 106 | inferred_complete_timeline |
| `Action_None` | 310 | 322 | 13 | inferred_complete_timeline |
| `Action_None` | 325 | 359 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 231 | 39 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 263 | 286 | 24 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 308 | 321 | 14 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 330 | 138 | inferred_complete_timeline |
| `Action_None` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |
| `Action_None` | 203 | 229 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 192 | 111 | inferred_complete_timeline |
| `Action_None` | 193 | 298 | 106 | inferred_complete_timeline |
| `Action_None` | 303 | 322 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 322 | 130 | inferred_complete_timeline |
| `Action_None` | 332 | 359 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 219 | 27 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 261 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 359 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 359 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 359 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 200 | 230 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 247 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 261 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 275 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–100 | 101 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–359 | 355 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–359 | 348 | 7 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–330 | 260 | 14 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 3–4 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–280 | 243 | 9 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 95–100 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 99–359 | 203 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 208–359 | 102 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 214–359 | 54 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 217–247 | 27 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 262–359 | 94 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 264–339 | 75 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 276–279 | 4 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 280–308 | 13 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 304–359 | 51 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 310–359 | 27 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `25` (3 segments found)
- ❌ Missing segment for action `Action_PullBlock` on target `24` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_PullBlock' for track '22' has invalid range: start=195, end=100. Clamping end to start.
- ⚠️ Action 'Action_None' range [193-330] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [195-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [247-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-293] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-331] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-286] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-321] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-308] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [193-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-236] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [238-257] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 264, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [264-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-47] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-152] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '19' starts at frame 193, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [193-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-322] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-124] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [233-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [251-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-353] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-336] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-341] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '32' has 1 frames without a visible bounding box.
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

</details>