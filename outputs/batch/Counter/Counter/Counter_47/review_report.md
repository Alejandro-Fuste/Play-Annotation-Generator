# Play-Annotation-Generator Annotation Review — Counter_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_47`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 189 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 184 | START | 184 | 196 |
| ✅ EXACT | `Action_DownBlock` | RT | `10` | `9` | 190 | START | 190 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `18` | 190 | START | 190 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 190 | START | 190 | 199 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `20` | `19` | 190 | START | 197 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 190 | START | 190 | 232 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 196 | END | 184 | 196 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 207 | START | 207 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `1` | 231 | START | 231 | 247 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 275 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–397
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_SnapReceive` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 206 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 230 | 24 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 397 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 212 | 29 | inferred_complete_timeline |
| `Action_None` | 215 | 333 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 323 | 140 | inferred_complete_timeline |
| `Action_None` | 344 | 347 | 4 | inferred_complete_timeline |
| `Action_None` | 349 | 356 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 247 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 284 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 286 | 479 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 190 | 232 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 239 | 275 | 37 | inferred_complete_timeline |
| `Action_None` | 276 | 479 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 203 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 275 | 54 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |
| `Action_None` | 331 | 336 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_BallSnap` | 184 | 196 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 197 | 275 | 79 | inferred_complete_timeline |
| `Action_None` | 276 | 331 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 209 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 258 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 262 | 264 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 275 | 86 | inferred_complete_timeline |
| `Action_None` | 276 | 346 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 215 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–372
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 297 | 114 | inferred_complete_timeline |
| `Action_None` | 299 | 321 | 23 | inferred_complete_timeline |
| `Action_None` | 325 | 372 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–386
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 386 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 226 | 43 | inferred_complete_timeline |
| `Action_None` | 232 | 270 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 249 | 66 | inferred_complete_timeline |
| `Action_None` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 265 | 349 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 267 | 84 | inferred_complete_timeline |
| `Action_None` | 269 | 314 | 46 | inferred_complete_timeline |
| `Action_None` | 316 | 447 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–400
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 323 | 140 | inferred_complete_timeline |
| `Action_None` | 326 | 400 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 207–211 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 218–252 | 22 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 235–343 | 38 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 249–338 | 87 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 264–479 | 210 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 271–400 | 114 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 273–287 | 11 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 365–367 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (5 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `20` (C): Annotated start 190 != Inferred start 197
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [184–196], lower_priority='Action_PullBlock' annotated_start=190, effective_Action_PullBlock_start=197.
- ⚠️ Action 'Action_BallCarry' range [231-247] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-479] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [190-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [234-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [239-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-479] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-479] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-372] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-346] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-447] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-323] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-400] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-397] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-386] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-349] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-258] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [262-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-331] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-215] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-312] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-326] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-338] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-406] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-400] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '30' has 1 frames without a visible bounding box.
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