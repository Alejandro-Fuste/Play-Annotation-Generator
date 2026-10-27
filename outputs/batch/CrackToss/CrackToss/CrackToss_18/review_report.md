# Play-Annotation-Generator Annotation Review — CrackToss_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_18`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 129
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | defense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 212 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 213 | START | 213 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | `18` | `17` | 216 | START | 216 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `2` | `1` | 216 | START | 216 | 261 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 228 | END | 213 | 228 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 229 | START | 229 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | `1` | `0` | 250 | START | 250 | 314 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 284 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–285
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 212 | 160 | inferred_complete_timeline |
| `Action_SnapReceive` | 213 | 228 | 16 | inferred_complete_timeline |
| `Action_Toss` | 229 | 249 | 21 | inferred_complete_timeline |
| `Action_None` | 250 | 285 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 258 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 288 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_CrackBlock` | 216 | 244 | 29 | inferred_complete_timeline |
| `Action_CrackBlock` | 248 | 284 | 37 | inferred_complete_timeline |
| `Action_None` | 285 | 312 | 28 | inferred_complete_timeline |
| `Action_None` | 315 | 354 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 291 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 212 | 117 | inferred_complete_timeline |
| `Action_None` | 213 | 240 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 212 | 162 | inferred_complete_timeline |
| `Action_BallSnap` | 213 | 228 | 16 | inferred_complete_timeline |
| `Action_None` | 229 | 312 | 84 | inferred_complete_timeline |
| `Action_None` | 349 | 389 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 335 | 123 | inferred_complete_timeline |
| `Action_None` | 337 | 347 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 261 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 268 | 271 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 272 | 60 | inferred_complete_timeline |
| `Action_None` | 275 | 287 | 13 | inferred_complete_timeline |
| `Action_None` | 370 | 389 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 243 | 31 | inferred_complete_timeline |
| `Action_None` | 245 | 296 | 52 | inferred_complete_timeline |
| `Action_None` | 300 | 308 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 226 | 14 | inferred_complete_timeline |
| `Action_None` | 239 | 265 | 27 | inferred_complete_timeline |
| `Action_None` | 276 | 284 | 9 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 222 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 233 | 21 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 290 | 46 | inferred_complete_timeline |
| `Action_None` | 294 | 359 | 66 | inferred_complete_timeline |
| `Action_None` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 284 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 270 | 58 | inferred_complete_timeline |
| `Action_None` | 272 | 373 | 102 | inferred_complete_timeline |
| `Action_None` | 380 | 381 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 244 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_BallCarry` | 250 | 314 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 316 | 323 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 382 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 212 | 114 | inferred_complete_timeline |
| `Action_None` | 213 | 316 | 104 | inferred_complete_timeline |
| `Action_None` | 318 | 327 | 10 | inferred_complete_timeline |
| `Action_None` | 330 | 332 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 188 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 204 | 10 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–73 | 28 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–211 | 112 | 11 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 238–304 | 67 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 240–389 | 146 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 253–352 | 73 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 257–297 | 28 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 281–364 | 24 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 283–389 | 82 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 292–389 | 86 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 351–354 | 4 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 352–388 | 33 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 364–389 | 26 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 366–389 | 23 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 378–389 | 12 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | 5 | 22 | 5 | 27.8% | 6–18 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [250-314] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [316-323] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-382] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [216-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [268-271] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-347] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-290] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-359] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-316] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-204] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-258] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-296] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-308] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-272] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [216-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-312] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-354] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-373] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-312] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-304] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-377] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-310] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-295] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-339] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-385] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-319] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-351] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-373] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-378] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>