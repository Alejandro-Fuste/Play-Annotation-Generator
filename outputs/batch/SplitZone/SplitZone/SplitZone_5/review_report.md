# Play-Annotation-Generator Annotation Review — SplitZone_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_5`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT3 | defense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | DT3 | `15` | `15` | 171 | START | 171 | 186 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 174 | START | 174 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 174 | START | 174 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 174 | START | 174 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 174 | START | 174 | 193 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 186 | END | 171 | 186 |
| ✅ EXACT | `Action_SplitBlock` | TE | `12` | `12` | 186 | START | 186 | 271 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 196 | START | 196 | 211 |
| ✅ EXACT | `Action_BallCarry` | RB | `21` | `21` | 212 | START | 212 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 271 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–410
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_SnapReceive` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 196 | 211 | 16 | inferred_complete_timeline |
| `Action_None` | 212 | 373 | 162 | inferred_complete_timeline |
| `Action_None` | 377 | 381 | 5 | inferred_complete_timeline |
| `Action_None` | 403 | 405 | 3 | inferred_complete_timeline |
| `Action_None` | 407 | 410 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 211 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 449 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 293 | 123 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 449 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 230 | 60 | inferred_complete_timeline |
| `Action_None` | 265 | 278 | 14 | inferred_complete_timeline |
| `Action_None` | 280 | 383 | 104 | inferred_complete_timeline |
| `Action_None` | 385 | 399 | 15 | inferred_complete_timeline |
| `Action_None` | 405 | 412 | 8 | inferred_complete_timeline |
| `Action_None` | 415 | 432 | 18 | inferred_complete_timeline |
| `Action_None` | 434 | 441 | 8 | inferred_complete_timeline |
| `Action_None` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 234 | 64 | inferred_complete_timeline |
| `Action_None` | 254 | 449 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_SplitBlock` | 186 | 271 | 86 | inferred_complete_timeline |
| `Action_None` | 272 | 357 | 86 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 390 | 29 | inferred_complete_timeline |
| `Action_None` | 395 | 398 | 4 | inferred_complete_timeline |
| `Action_None` | 401 | 408 | 8 | inferred_complete_timeline |
| `Action_None` | 411 | 412 | 2 | inferred_complete_timeline |
| `Action_None` | 414 | 420 | 7 | inferred_complete_timeline |
| `Action_None` | 423 | 427 | 5 | inferred_complete_timeline |
| `Action_None` | 430 | 437 | 8 | inferred_complete_timeline |
| `Action_None` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 271 | 98 | inferred_complete_timeline |
| `Action_None` | 272 | 449 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 193 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 214 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 197 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 271 | 53 | inferred_complete_timeline |
| `Action_None` | 272 | 443 | 172 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 253 | 83 | inferred_complete_timeline |
| `Action_None` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 262 | 92 | inferred_complete_timeline |
| `Action_None` | 264 | 449 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 191 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 238 | 68 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 449 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 187 | 198 | 12 | inferred_complete_timeline |
| `Action_None` | 219 | 390 | 172 | inferred_complete_timeline |
| `Action_None` | 397 | 449 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 242 | 72 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 393 | 122 | inferred_complete_timeline |
| `Action_None` | 396 | 449 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 449 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 256 | 86 | inferred_complete_timeline |
| `Action_None` | 258 | 278 | 21 | inferred_complete_timeline |
| `Action_None` | 282 | 285 | 4 | inferred_complete_timeline |
| `Action_None` | 289 | 449 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 240 | 70 | inferred_complete_timeline |
| `Action_None` | 242 | 414 | 173 | inferred_complete_timeline |
| `Action_None` | 417 | 449 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 449 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 449 | 279 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–201 | 202 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 217–449 | 229 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 229–241 | 13 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 231–449 | 211 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 232–446 | 179 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 264–449 | 186 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 349–449 | 68 | 11 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 354–355 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 358–387 | 23 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 373–375 | 3 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 400–443 | 22 | 3 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 409–411 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 426–437 | 10 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 437–449 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 12: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 98 frames exceeds threshold 90 frames [start=174, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 98 frames exceeds threshold 90 frames [start=174, end=271].
- ⚠️ Action 'Action_None' range [171-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-293] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-414] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-278] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-383] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-399] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-412] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-432] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-441] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-278] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-393] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-357] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-390] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-420] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-437] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-373] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-390] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-443] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-238] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-253] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-393] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-449] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-392] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-446] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-393] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-429] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-441] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-364] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-382] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-375] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-421] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>