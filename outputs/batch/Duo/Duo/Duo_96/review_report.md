# Play-Annotation-Generator Annotation Review — Duo_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_96`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DT1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR2 | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `22` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 14 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `10` | `10` | 237 | START | 237 | 248 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DT1 | `11` | `11` | 237 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR2 | `16` | `16` | 237 | START | 237 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `7` | `7` | 237 | START | 237 | 275 |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | `14` | `14` | 256 | START | 256 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `22` | `20` | 256 | START | 256 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 311 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 255 | 206 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 256 | 311 | 56 | inferred_complete_timeline |
| `Action_None` | 312 | 358 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 121 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 172 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 242 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 358 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 250 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 358 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 14–266
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 236 | 223 | inferred_complete_timeline |
| `Action_ComboBlock` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 247 | 266 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 172 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 249 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 259 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 358 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 237 | 248 | 12 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 266 | 11 | inferred_complete_timeline |
| `Action_ComboBlock` | 268 | 311 | 44 | inferred_complete_timeline |
| `Action_None` | 312 | 341 | 30 | inferred_complete_timeline |
| `Action_None` | 344 | 358 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_ComboBlock` | 237 | 275 | 39 | inferred_complete_timeline |
| `Action_ComboBlock` | 278 | 280 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 284 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 358 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 305 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 357 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 73 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 357 | 358 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–256
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 256 | 245 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–358 | 359 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 107–227 | 43 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 196–315 | 113 | 6 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 241–265 | 22 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 241–339 | 87 | 5 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 287–328 | 18 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 288–358 | 71 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 288–358 | 71 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 297–315 | 19 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 324–340 | 17 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 327–341 | 6 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 334–358 | 25 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 337–354 | 16 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 339–358 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `11` (DT1)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 194: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '11' has invalid range: start=237, end=73. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-357] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-358] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [237-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [278-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-172] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-249] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [237-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [256-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-341] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-121] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-186] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-242] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-255] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-358] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-236] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '16' starts at frame 237, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [237-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [247-266] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-220] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-312] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-255] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [256-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [260-311] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-327] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-300] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-315] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-340] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>