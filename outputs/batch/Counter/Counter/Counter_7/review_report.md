# Play-Annotation-Generator Annotation Review — Counter_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_7`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | defense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 205 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 206 | START | 206 | 208 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 208 | END | 206 | 208 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `1` | `0` | 213 | START | 213 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `18` | `17` | 217 | START | 217 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `19` | 217 | START | 217 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | `7` | `6` | 217 | START | 217 | 226 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `16` | `15` | 217 | START | 219 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT1 | `2` | `1` | 217 | START | 217 | 256 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 240 | START | 240 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 250 | START | 250 | 276 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 303 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–388
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 145 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 205 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 240 | 249 | 10 | inferred_complete_timeline |
| `Action_None` | 250 | 388 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 213 | 249 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 276 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 389 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 216 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 217 | 226 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 234 | 297 | 64 | inferred_complete_timeline |
| `Action_DownBlock` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 304 | 389 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 389 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 389 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 216 | 128 | inferred_complete_timeline |
| `Action_DownBlock` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 240 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 245 | 252 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 275 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 279 | 303 | 25 | inferred_complete_timeline |
| `Action_None` | 304 | 322 | 19 | inferred_complete_timeline |
| `Action_None` | 324 | 348 | 25 | inferred_complete_timeline |
| `Action_None` | 351 | 357 | 7 | inferred_complete_timeline |
| `Action_None` | 363 | 389 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 54 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 205 | 135 | inferred_complete_timeline |
| `Action_BallSnap` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 216 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 219 | 243 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 389 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 217 | 256 | 40 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 259 | 294 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 297 | 303 | 7 | inferred_complete_timeline |
| `Action_None` | 304 | 389 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 12 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 205 | 118 | inferred_complete_timeline |
| `Action_None` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 270 | 65 | inferred_complete_timeline |
| `Action_None` | 301 | 389 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 251 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 265 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 311 | 106 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 389 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 206 | 273 | 68 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 12 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 205 | 125 | inferred_complete_timeline |
| `Action_None` | 206 | 363 | 158 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 92–289 | 148 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 92–389 | 274 | 8 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 100–273 | 122 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 111–389 | 204 | 10 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 282–389 | 92 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 299–362 | 63 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 301–389 | 89 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 320–389 | 69 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 321–345 | 14 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 329–389 | 52 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 378–389 | 11 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 379–389 | 9 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (4 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `16` (C): Annotated start 217 != Inferred start 219
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 16: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [250-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [217-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [259-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-389] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [217-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [234-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [300-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [240-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-12] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-363] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-54] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [219-243] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-12] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '17' starts at frame 217, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [217-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [245-252] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [260-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [279-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-322] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-348] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [217-226] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-252] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [255-274] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [279-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-369] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-205] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-354] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-358] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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