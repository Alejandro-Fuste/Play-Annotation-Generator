# Play-Annotation-Generator Annotation Review — Power_329

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_329`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 178
- **Validation Warnings:** 211
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 0
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `28` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `29` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `32` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `28` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 8 | START | 8 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 8 | START | 8 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 8 | START | 8 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 8 | START | 10 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 8 | START | 10 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `25` | `Group` | 8 | START | 22 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `28` | `Group` | 8 | START | 34 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `29` | `Group` | 8 | START | 135 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `32` | `Group` | 8 | START | 140 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 8 | START | 8 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 213 | START | 213 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `17` | 213 | START | 213 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `28` | `22` | 213 | START | 213 | 214 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 256 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 284 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 304 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 347 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–233
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 233 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–344
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 324 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 344 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–210
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 44 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `29`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 135–210
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 135 | 210 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `25`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 22–389
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 218 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 262 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 389 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `28`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 34–389
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 117 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 212 | 83 | inferred_complete_timeline |
| `Action_PullBlock` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 247 | 255 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 257 | 287 | 31 | inferred_complete_timeline |
| `Action_None` | 288 | 319 | 32 | inferred_complete_timeline |
| `Action_None` | 322 | 337 | 16 | inferred_complete_timeline |
| `Action_None` | 339 | 347 | 9 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–387
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 212 | 205 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 279 | 287 | 9 | inferred_complete_timeline |
| `Action_None` | 288 | 359 | 72 | inferred_complete_timeline |
| `Action_None` | 365 | 387 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–218
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 32 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 212 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 218 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `32`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `32`
- **team_side:** `offense`
- **Visible Frames:** 140–210
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 140 | 206 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–294
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 246 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 267 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 294 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `26`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 29–62
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 51 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 62 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 44 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 214 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 285 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 389 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 341 | 334 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 350 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 356 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–302
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 260 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 302 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 8–227
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 220 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 227 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 337 | 330 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–302
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 276 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 302 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 8–389 | 346 | 10 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 8–210 | 193 | 4 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 8–105 | 98 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 8–389 | 377 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 8–79 | 67 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 13–389 | 360 | 7 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 22–389 | 234 | 13 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 180–334 | 150 | 5 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 243–264 | 8 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 246–389 | 65 | 9 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 255–332 | 45 | 5 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 265–389 | 122 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 272–389 | 105 | 4 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 280–389 | 108 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 303–389 | 42 | 7 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 329–377 | 49 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 354–389 | 32 | 2 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 366–389 | 24 | 1 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `28` (3 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 165 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 658: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 658: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [8-324] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-271] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-347] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-254] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-284] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-92] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-104] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-111] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-285] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-337] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-345] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-389] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-260] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-295] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-348] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-384] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-284] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-347] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-356] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-341] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-238] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [245-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [257-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-44] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-32] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-36] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-51] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-243] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-302] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-40] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-282] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-218] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-51] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-69] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-85] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-117] for track '22' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-128] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [213-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [247-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-319] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-337] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-347] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-206] for track '24' has 11 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-212] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-315] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-334] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-255] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-274] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-347] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-389] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-320] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-347] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-377] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-389] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>