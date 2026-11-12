# Play-Annotation-Generator Annotation Review — SplitZone_265

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_265`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DE1 | defense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `25` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 26 | START | 26 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 26 | START | 26 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 26 | START | 26 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 26 | START | 26 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 26 | START | 26 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 26 | START | 26 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `24` | `Group` | 26 | START | 79 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 26 | START | 26 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 26 | START | 26 | 171 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 134 | START | 134 | 231 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 134 | START | 134 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 134 | START | 134 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `24` | `22` | 134 | START | 134 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DE1 | `11` | `11` | 141 | START | 141 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 142 | END | 142 | 142 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 156 | START | 156 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `25` | `23` | 157 | START | 163 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 170 | START | 170 | 397 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 26–336
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 141 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_None` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 156 | 169 | 14 | inferred_complete_timeline |
| `Action_None` | 170 | 336 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–418
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 169 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 397 | 228 | inferred_complete_timeline |
| `Action_BallCarry` | 399 | 418 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 211 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 248 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 266 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 283 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 419 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 321 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 419 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 26–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 171 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 187 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 419 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–415
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 67 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 133 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 155 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 210 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 379 | 147 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 400 | 407 | 8 | inferred_complete_timeline |
| `Action_None` | 412 | 415 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 26–145
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 133 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 145 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 26–413
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 133 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 231 | 98 | inferred_complete_timeline |
| `Action_None` | 233 | 382 | 150 | inferred_complete_timeline |
| `Action_None` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_None` | 395 | 413 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 79–287
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 79 | 133 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 232 | 99 | inferred_complete_timeline |
| `Action_None` | 233 | 287 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–199
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 140 | 115 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_SplitBlock` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 199 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–153
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 145 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 27–330
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 189 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 330 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 26–419
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 217 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 332 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 342 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 391 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 419 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–374
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 261 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 356 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 374 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–366
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 303 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 349 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 358 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 366 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–406
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 330 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 366 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 389 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 398 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 406 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–200
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 200 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–390
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 390 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–385
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 376 | 351 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 385 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–280
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 186 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 235 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 280 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 26–419 | 343 | 7 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 26–419 | 373 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 29–41 | 13 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 163–417 | 231 | 7 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 199–419 | 202 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 225–227 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 232–419 | 170 | 10 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 288–324 | 32 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 293–419 | 108 | 5 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 301–374 | 69 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 339–419 | 70 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 354–419 | 63 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 385–417 | 26 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 400–419 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `25` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 532: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 532: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '22' (RT) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
- ⚠️ Action 'Action_PreSnap' range [26-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-266] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-293] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-341] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-321] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-397] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [399-418] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-390] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-235] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-280] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-376] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-187] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-349] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-366] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-330] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-366] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-382] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-406] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [141-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [153-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [165-199] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-356] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-231] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-382] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-413] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-332] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-342] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-391] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-145] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-220] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [231-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-379] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-407] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-415] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-59] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-242] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-334] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-55] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-330] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-287] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [163-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [169-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-348] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-393] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-410] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-288] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-351] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-381] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-390] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-400] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-407] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-349] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-376] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-366] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-407] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-419] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-391] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-407] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-417] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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