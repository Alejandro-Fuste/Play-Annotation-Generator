# Play-Annotation-Generator Annotation Review — Counter_285

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_285`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 140 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 141 | START | 141 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `14` | `13` | 144 | START | 144 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 144 | START | 158 | 163 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `17` | 144 | START | 144 | 240 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `19` | `18` | 144 | START | 144 | 216 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 157 | END | 141 | 157 |
| ✅ EXACT | `Action_BallCarry` | QB | `17` | `16` | 188 | START | 188 | 374 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 240 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 157 | 17 | inferred_complete_timeline |
| `Action_None` | 158 | 187 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 374 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 140 | 54 | inferred_complete_timeline |
| `Action_None` | 141 | 183 | 43 | inferred_complete_timeline |
| `Action_None` | 186 | 293 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–385
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 385 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 144 | 216 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 240 | 97 | inferred_complete_timeline |
| `Action_None` | 241 | 279 | 39 | inferred_complete_timeline |
| `Action_None` | 299 | 389 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 157 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 240 | 76 | inferred_complete_timeline |
| `Action_None` | 241 | 273 | 33 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 230 | 90 | inferred_complete_timeline |
| `Action_None` | 232 | 252 | 21 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 173 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 186 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 240 | 53 | inferred_complete_timeline |
| `Action_None` | 241 | 286 | 46 | inferred_complete_timeline |
| `Action_None` | 290 | 350 | 61 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 358 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 250 | 110 | inferred_complete_timeline |
| `Action_None` | 254 | 389 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 178 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 195 | 55 | inferred_complete_timeline |
| `Action_None` | 200 | 389 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 281 | 141 | inferred_complete_timeline |
| `Action_None` | 286 | 355 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 267 | 127 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 308 | 32 | inferred_complete_timeline |
| `Action_None` | 310 | 313 | 4 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 380 | 60 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 194 | 54 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 304 | 164 | inferred_complete_timeline |
| `Action_None` | 306 | 389 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 297 | 157 | inferred_complete_timeline |
| `Action_None` | 303 | 324 | 22 | inferred_complete_timeline |
| `Action_None` | 326 | 337 | 12 | inferred_complete_timeline |
| `Action_None` | 343 | 352 | 10 | inferred_complete_timeline |
| `Action_None` | 356 | 362 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 16–37 | 19 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 207–389 | 167 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 221–299 | 75 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 245–389 | 145 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 261–355 | 85 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 288–389 | 102 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 314–320 | 7 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 350–368 | 18 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 361–389 | 27 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 571: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RT) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [141–157], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=158.
- ⚠️ Action 'Action_None' range [141-385] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-337] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-362] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-195] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-293] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-173] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [188-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-350] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-267] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-380] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-355] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-374] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-240] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [144-216] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-252] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-33] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-342] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-355] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-385] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>