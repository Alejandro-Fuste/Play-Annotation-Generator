# Play-Annotation-Generator Annotation Review — CrackToss_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_6`
- **Frame Range:** 0 to 388 (389 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 388
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `18` |
| ✅ EXACT | `Action_PullBlock` | WR | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `27` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 206 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `22` | `18` | 207 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | WR | `1` | `0` | 211 | START | 211 | 299 |
| ✅ EXACT | `Action_SnapReceive` | LT | `15` | `14` | 212 | END | 207 | 212 |
| ✅ EXACT | `Action_Toss` | LT | `15` | `14` | 217 | START | 217 | 248 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `27` | `21` | 221 | START | 221 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `11` | `10` | 249 | START | 249 | 332 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 299 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 206 | 147 | inferred_complete_timeline |
| `Action_None` | 207 | 226 | 20 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 276 | 36 | inferred_complete_timeline |
| `Action_None` | 278 | 388 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PullBlock` | 211 | 299 | 89 | inferred_complete_timeline |
| `Action_None` | 300 | 388 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 267 | 61 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 206 | 110 | inferred_complete_timeline |
| `Action_SnapReceive` | 207 | 212 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_Toss` | 217 | 248 | 32 | inferred_complete_timeline |
| `Action_None` | 249 | 277 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 206 | 80 | inferred_complete_timeline |
| `Action_None` | 207 | 265 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 332 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 339 | 347 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 351 | 353 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 358 | 388 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 302 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 383 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 388 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 206 | 141 | inferred_complete_timeline |
| `Action_None` | 207 | 302 | 96 | inferred_complete_timeline |
| `Action_None` | 307 | 313 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 225 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 206 | 129 | inferred_complete_timeline |
| `Action_None` | 207 | 278 | 72 | inferred_complete_timeline |
| `Action_None` | 286 | 364 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 300 | 94 | inferred_complete_timeline |
| `Action_None` | 303 | 388 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 304 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_None` | 207 | 357 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–135 | 136 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–156 | 157 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 77–97 | 12 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 99–388 | 284 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 175–388 | 156 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 188–306 | 119 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 191–324 | 133 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 225–255 | 25 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 229–388 | 160 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 238–285 | 48 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 253–388 | 104 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 281–379 | 99 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 282–388 | 107 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 284–291 | 8 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 292–388 | 94 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 312–323 | 8 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 338–344 | 7 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 356–388 | 33 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 379–388 | 10 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 381–388 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 14: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 14: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=207, end=97. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-383] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-364] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-313] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-300] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-332] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-337] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [339-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [351-353] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [358-388] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-276] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-277] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-265] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-388] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-388] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-324] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-388] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>