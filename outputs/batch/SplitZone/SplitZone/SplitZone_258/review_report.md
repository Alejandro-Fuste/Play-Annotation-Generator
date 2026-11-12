# Play-Annotation-Generator Annotation Review — SplitZone_258

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_258`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 3
- **Action Segments:** 63
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 25 | START | 26 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 25 | START | 26 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 25 | START | 26 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 25 | START | 26 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 25 | START | 26 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 25 | START | 26 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 25 | START | 26 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 25 | START | 26 | 195 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 193 | START | 193 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 196 | START | 196 | 307 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 196 | START | 196 | 220 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 196 | START | 201 | 307 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 196 | START | 196 | 302 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 196 | START | 196 | 307 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `12` | `12` | 200 | END | 193 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `10` | `10` | 209 | START | 209 | 231 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 218 | START | 218 | 228 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `13` | `13` | 221 | START | 221 | 307 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 229 | START | 229 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 307 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 26–284
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 134 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 192 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 217 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 218 | 228 | 11 | inferred_complete_timeline |
| `Action_None` | 229 | 284 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 26–312
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 228 | 203 | inferred_complete_timeline |
| `Action_BallCarry` | 229 | 245 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 279 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 281 | 309 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 389 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 26–293
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 208 | 183 | inferred_complete_timeline |
| `Action_SplitBlock` | 209 | 231 | 23 | inferred_complete_timeline |
| `Action_SplitBlock` | 234 | 248 | 15 | inferred_complete_timeline |
| `Action_SplitBlock` | 257 | 293 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 26–302
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 195 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 302 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 26–325
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 195 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 307 | 112 | inferred_complete_timeline |
| `Action_None` | 308 | 325 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 26–322
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_BallSnap` | 193 | 200 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 307 | 107 | inferred_complete_timeline |
| `Action_None` | 308 | 322 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 26–360
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 195 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 307 | 112 | inferred_complete_timeline |
| `Action_None` | 308 | 342 | 35 | inferred_complete_timeline |
| `Action_None` | 355 | 360 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 26–386
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 195 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 220 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 221 | 307 | 87 | inferred_complete_timeline |
| `Action_None` | 308 | 386 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–271
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 271 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–364
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 364 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–323
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 323 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 389 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 26–317
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 317 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 26–320
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 320 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–314
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 314 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–297
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 193 | 297 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 132–219 | 88 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 260–389 | 130 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 279–282 | 4 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 282–389 | 108 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 313–316 | 4 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 325–372 | 48 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 377–389 | 13 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 382–389 | 8 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 26 | 192 | 167 | 100.0% | None |
| `18` | `20` | 107 | 107 | 1 | 100.0% | None |
| `19` | `21` | 130 | 131 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 196 != Inferred start 201
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=196, end=302].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 112 frames exceeds threshold 90 frames [start=196, end=307].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [193–200], lower_priority='Action_ZoneBlock' annotated_start=196, effective_Action_ZoneBlock_start=201.
- ⚠️ Action 'Action_None' range [193-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-317] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-314] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-364] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-271] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-342] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [209-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [234-248] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [257-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [193-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-386] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-307] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-322] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-192] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-372] for track '26' has 1 frames without a visible bounding box.
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

</details>