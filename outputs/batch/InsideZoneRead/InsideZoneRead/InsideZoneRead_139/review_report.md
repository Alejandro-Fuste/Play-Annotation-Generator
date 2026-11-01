# Play-Annotation-Generator Annotation Review — InsideZoneRead_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_139`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 232 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 185 | START | 185 | 199 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 188 | START | 188 | 292 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 188 | START | 188 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `3` | 188 | START | 200 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 188 | START | 188 | 292 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 188 | START | 188 | 292 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `11` | `10` | 199 | END | 185 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | DE2 | `11` | `10` | 206 | START | 206 | 214 |
| ✅ EXACT | `Action_Handoff` | DE2 | `11` | `10` | 222 | START | 222 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `13` | `12` | 237 | START | 237 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 239 | START | 239 | 247 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 292 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 247 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 286 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 292 | 105 | inferred_complete_timeline |
| `Action_None` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 292 | 105 | inferred_complete_timeline |
| `Action_None` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_BallSnap` | 185 | 199 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 292 | 53 | inferred_complete_timeline |
| `Action_None` | 293 | 355 | 63 | inferred_complete_timeline |
| `Action_None` | 370 | 389 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–383
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 236 | 49 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 237 | 289 | 53 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 292 | 292 | 1 | inferred_complete_timeline |
| `Action_None` | 293 | 302 | 10 | inferred_complete_timeline |
| `Action_None` | 305 | 346 | 42 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_None` | 363 | 383 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 292 | 105 | inferred_complete_timeline |
| `Action_None` | 293 | 293 | 1 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 389 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 307 | 123 | inferred_complete_timeline |
| `Action_None` | 310 | 345 | 36 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |
| `Action_None` | 354 | 356 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_SnapReceive` | 185 | 199 | 15 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 206 | 214 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 222 | 238 | 17 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 336 | 152 | inferred_complete_timeline |
| `Action_None` | 349 | 389 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 259 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 292 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 389 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 184–256 | 73 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 197–388 | 188 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 250–365 | 93 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 264–385 | 91 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 264–270 | 7 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 277–344 | 64 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 290–301 | 12 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 305–389 | 81 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 314–389 | 65 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 315–324 | 9 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 331–389 | 59 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 334–337 | 4 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 345–389 | 45 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 372–389 | 17 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 278: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (C) duration 105 frames exceeds threshold 90 frames [start=188, end=292].
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [185–199], lower_priority='Action_ZoneBlock' annotated_start=188, effective_Action_ZoneBlock_start=200.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 105 frames exceeds threshold 90 frames [start=188, end=292].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 105 frames exceeds threshold 90 frames [start=188, end=292].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 105 frames exceeds threshold 90 frames [start=188, end=292].
- ⚠️ Action 'Action_None' range [185-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-292] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [200-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-292] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-355] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-307] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-345] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 293, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [293-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-286] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [206-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [237-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-346] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-383] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-256] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-370] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-388] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-298] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-344] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-334] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-385] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-338] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-301] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-374] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-335] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>