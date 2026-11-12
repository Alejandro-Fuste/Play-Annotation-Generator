# Play-Annotation-Generator Annotation Review — SplitZone_214

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_214`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | defense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE2 | defense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 165 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `18` | `18` | 233 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 236 | START | 236 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 236 | START | 236 | 352 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 236 | START | 236 | 278 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 236 | START | 236 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `7` | 236 | START | 236 | 356 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `17` | `17` | 239 | END | 233 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | `11` | `11` | 248 | START | 248 | 338 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `17` | `17` | 260 | START | 260 | 266 |
| ✅ EXACT | `Action_BallCarry` | RT | `3` | `3` | 272 | START | 272 | 479 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE2 | `14` | `14` | 275 | START | 275 | 346 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 432 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 377 | 145 | inferred_complete_timeline |
| `Action_None` | 379 | 479 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 232 | 65 | inferred_complete_timeline |
| `Action_None` | 233 | 479 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 232 | 51 | inferred_complete_timeline |
| `Action_None` | 233 | 265 | 33 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 298 | 9 | inferred_complete_timeline |
| `Action_None` | 300 | 311 | 12 | inferred_complete_timeline |
| `Action_None` | 313 | 479 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 278 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 432 | 148 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 291 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 304 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 323 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 356 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 386 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 352 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 356 | 379 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 271 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 479 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 368 | 136 | inferred_complete_timeline |
| `Action_None` | 371 | 479 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–400
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 274 | 118 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 275 | 346 | 72 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 350 | 400 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 252 | 278 | 27 | inferred_complete_timeline |
| `Action_None` | 280 | 287 | 8 | inferred_complete_timeline |
| `Action_None` | 300 | 316 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 262 | 30 | inferred_complete_timeline |
| `Action_None` | 264 | 334 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_SplitBlock` | 248 | 338 | 91 | inferred_complete_timeline |
| `Action_SplitBlock` | 341 | 353 | 13 | inferred_complete_timeline |
| `Action_SplitBlock` | 360 | 417 | 58 | inferred_complete_timeline |
| `Action_SplitBlock` | 422 | 432 | 11 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 232 | 23 | inferred_complete_timeline |
| `Action_None` | 233 | 339 | 107 | inferred_complete_timeline |
| `Action_None` | 347 | 351 | 5 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 287 | 55 | inferred_complete_timeline |
| `Action_None` | 289 | 350 | 62 | inferred_complete_timeline |
| `Action_None` | 386 | 388 | 3 | inferred_complete_timeline |
| `Action_None` | 395 | 479 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_None` | 233 | 342 | 110 | inferred_complete_timeline |
| `Action_None` | 407 | 479 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–477 | 381 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–26 | 16 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 118–137 | 16 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 155–354 | 143 | 7 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 265–479 | 201 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 266–479 | 214 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 285–317 | 33 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 292–357 | 66 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 336–479 | 131 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 350–479 | 72 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 355–479 | 117 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 358–479 | 122 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 364–387 | 24 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 365–398 | 34 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 391–417 | 24 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 397–479 | 77 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 402–479 | 78 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 407–479 | 71 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 420–423 | 4 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 431–479 | 49 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 432–474 | 43 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `18` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 197 frames exceeds threshold 90 frames [start=236, end=432].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (C) duration 151 frames exceeds threshold 90 frames [start=236, end=386].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '14' (DE2) duration 126 frames exceeds threshold 90 frames [start=275, end=400].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 144 frames exceeds threshold 90 frames [start=236, end=379].
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=233, end=26. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-342] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-278] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 233, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [233-235] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-350] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-356] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [363-386] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-368] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [248-338] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [341-353] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [360-417] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [302-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-323] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [275-346] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [350-400] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-265] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-298] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-352] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [356-379] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [260-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-477] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-354] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-317] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-341] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-407] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-357] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-455] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-371] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-407] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-387] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-398] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-417] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-426] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-423] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-474] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>