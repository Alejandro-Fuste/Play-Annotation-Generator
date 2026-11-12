# Play-Annotation-Generator Annotation Review — SplitZone_186

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_186`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `21` | `Group` | 0 | START | 43 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 208 |
| ✅ EXACT | `Action_BallSnap` | QB | `11` | `11` | 209 | START | 209 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 212 | START | 212 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 212 | START | 212 | 319 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 212 | START | 212 | 334 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `23` | `22` | 214 | END | 209 | 214 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `13` | `13` | 217 | START | 217 | 261 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `23` | `22` | 233 | START | 233 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 244 | START | 244 | 286 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 334 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_BallSnap` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 215 | 313 | 99 | inferred_complete_timeline |
| `Action_None` | 319 | 419 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_BallCarry` | 244 | 286 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 419 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 419 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_SplitBlock` | 217 | 261 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 295 | 87 | inferred_complete_timeline |
| `Action_None` | 299 | 419 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 43–306
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 208 | 166 | inferred_complete_timeline |
| `Action_None` | 209 | 268 | 60 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 306 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 290 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 311 | 334 | 24 | inferred_complete_timeline |
| `Action_None` | 335 | 419 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 334 | 123 | inferred_complete_timeline |
| `Action_None` | 335 | 403 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–410
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 319 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 326 | 334 | 9 | inferred_complete_timeline |
| `Action_None` | 335 | 410 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 233 | 25 | inferred_complete_timeline |
| `Action_None` | 247 | 302 | 56 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 225 | 17 | inferred_complete_timeline |
| `Action_None` | 248 | 300 | 53 | inferred_complete_timeline |
| `Action_None` | 304 | 308 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 334 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 208 | 123 | inferred_complete_timeline |
| `Action_None` | 209 | 229 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–394
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 394 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 419 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 252 | 44 | inferred_complete_timeline |
| `Action_None` | 258 | 270 | 13 | inferred_complete_timeline |
| `Action_None` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 419 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 364 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 419 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–29 | 30 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–419 | 420 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 20–55 | 36 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 40–41 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–318 | 116 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 120–138 | 19 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 233–419 | 184 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 238–303 | 6 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 244–419 | 166 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 244–251 | 6 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 258–419 | 158 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 326–335 | 7 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 336–419 | 84 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 342–419 | 69 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 348–419 | 72 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 362–366 | 4 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 366–368 | 3 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 374–384 | 11 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 383–419 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF3` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 374: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
- ⚠️ Action 'Action_ZoneBlock' range [212-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [305-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [311-334] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [244-286] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-403] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-270] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-364] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-410] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [217-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-394] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-300] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-334] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-318] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-313] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-362] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-384] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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