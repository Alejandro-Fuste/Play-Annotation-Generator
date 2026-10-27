# Play-Annotation-Generator Annotation Review — Dagger_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_32`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 419
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 4 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 179 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 180 | START | 180 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 183 | START | 185 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 184 | END | 180 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR1 | `1` | `1` | 201 | START | 201 | 226 |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | `4` | `4` | 201 | START | 201 | 277 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `8` | `8` | 280 | START | N/A | N/A |

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
- **Visible Frames:** 0–363
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_SnapReceive` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 219 | 31 | inferred_complete_timeline |
| `Action_None` | 223 | 273 | 51 | inferred_complete_timeline |
| `Action_None` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 217 | 38 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 253 | 262 | 10 | inferred_complete_timeline |
| `Action_None` | 266 | 321 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_BreakInside` | 201 | 226 | 26 | inferred_complete_timeline |
| `Action_BreakInside` | 228 | 324 | 97 | inferred_complete_timeline |
| `Action_None` | 325 | 348 | 24 | inferred_complete_timeline |
| `Action_None` | 357 | 419 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_ClearToEdge` | 201 | 277 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–233
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 114 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 179 | 27 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 225 | 9 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–201
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 179 | 176 | inferred_complete_timeline |
| `Action_BallSnap` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 179 | 167 | inferred_complete_timeline |
| `Action_None` | 180 | 367 | 188 | inferred_complete_timeline |
| `Action_None` | 370 | 419 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 213 | 34 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 255 | 419 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 336 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 232 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 368 | 189 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 368 | 189 | inferred_complete_timeline |
| `Action_None` | 370 | 382 | 13 | inferred_complete_timeline |
| `Action_None` | 403 | 411 | 9 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–419 | 411 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 205–249 | 30 | 3 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 222–278 | 43 | 6 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 226–412 | 175 | 5 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 301–307 | 7 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 314–419 | 104 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 324–341 | 18 | 1 | Undefined position; Undefined team |
| `22` | `37` | Position_Unknown | Team_Unknown | 342–344 | 3 | 1 | Undefined position; Undefined team |
| `23` | `45` | Position_Unknown | Team_Unknown | 347–419 | 73 | 1 | Undefined position; Undefined team |
| `24` | `47` | Position_Unknown | Team_Unknown | 348–368 | 21 | 1 | Undefined position; Undefined team |
| `25` | `53` | Position_Unknown | Team_Unknown | 404–419 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BreakInside` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `8` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 34: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [180–184], lower_priority='Action_PassBlock' annotated_start=183, effective_Action_PassBlock_start=185.
- ⚠️ Action 'Action_None' range [180-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-321] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [201-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [228-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-368] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-336] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [201-277] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-368] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-382] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-411] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 180, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [180-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [200-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-367] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-249] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-398] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-345] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-341] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>