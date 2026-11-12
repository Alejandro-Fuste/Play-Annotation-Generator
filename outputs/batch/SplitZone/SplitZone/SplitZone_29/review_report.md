# Play-Annotation-Generator Annotation Review — SplitZone_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_29`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 14 | START | 14 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 14 | START | 14 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 14 | START | 14 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 14 | START | 14 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 14 | START | 14 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 14 | START | 14 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 14 | START | 14 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 14 | START | 14 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 14 | START | 32 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 14 | START | 64 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 14 | START | 14 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `19` | `19` | 244 | START | 244 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 247 | START | 247 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 247 | START | 247 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 247 | START | 262 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 247 | START | 247 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `23` | `21` | 247 | START | 247 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `13` | `13` | 253 | START | 253 | 307 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 261 | END | 244 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 270 | START | 270 | 276 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 270 | START | 270 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 323 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 52 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 243 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 244 | 261 | 18 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 270 | 389 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 14–386
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 269 | 256 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 279 | 303 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 323 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 326 | 354 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 376 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 380 | 381 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 383 | 386 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 252 | 239 | inferred_complete_timeline |
| `Action_SplitBlock` | 253 | 307 | 55 | inferred_complete_timeline |
| `Action_SplitBlock` | 315 | 323 | 9 | inferred_complete_timeline |
| `Action_None` | 324 | 389 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–388
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 246 | 233 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 293 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 323 | 24 | inferred_complete_timeline |
| `Action_None` | 324 | 324 | 1 | inferred_complete_timeline |
| `Action_None` | 330 | 388 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 246 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 260 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 290 | 298 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 303 | 323 | 21 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 14–283
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 24 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 243 | 185 | inferred_complete_timeline |
| `Action_BallSnap` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 278 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 283 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 64–342
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 64 | 246 | 183 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 261 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 310 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 323 | 6 | inferred_complete_timeline |
| `Action_None` | 324 | 334 | 11 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 20 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 85 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 246 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 270 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 323 | 52 | inferred_complete_timeline |
| `Action_None` | 324 | 389 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 275 | 32 | inferred_complete_timeline |
| `Action_None` | 280 | 389 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 284 | 41 | inferred_complete_timeline |
| `Action_None` | 303 | 389 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–387
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 295 | 52 | inferred_complete_timeline |
| `Action_None` | 310 | 328 | 19 | inferred_complete_timeline |
| `Action_None` | 338 | 387 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 291 | 48 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 389 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 389 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–380
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 244 | 364 | 121 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 380 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 283–304 | 22 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 339–351 | 4 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 348–389 | 27 | 5 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 353–389 | 33 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 377–379 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `23` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [244–261], lower_priority='Action_ZoneBlock' annotated_start=247, effective_Action_ZoneBlock_start=262.
- ⚠️ Action 'Action_None' range [244-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-291] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-364] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-380] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [253-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-328] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-276] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [279-303] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [326-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [362-376] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [380-381] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-386] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-323] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 324, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [324-324] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-388] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-46] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-54] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-270] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-323] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [244-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [262-278] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-260] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [290-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-246] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [271-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-310] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-334] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-304] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-372] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-385] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '27' has 1 frames without a visible bounding box.
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

</details>