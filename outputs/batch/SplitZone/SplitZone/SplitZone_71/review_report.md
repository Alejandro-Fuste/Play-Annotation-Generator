# Play-Annotation-Generator Annotation Review — SplitZone_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_71`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `22` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 13 | START | 14 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 13 | START | 14 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 13 | START | 14 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 13 | START | 14 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 13 | START | 14 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 13 | START | 14 | 204 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 202 | START | 202 | 215 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `4` | `4` | 204 | START | 204 | 251 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 205 | START | 205 | 251 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 205 | START | 216 | 251 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `17` | 205 | START | 205 | 251 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 205 | START | 205 | 251 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 205 | START | 205 | 224 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 215 | END | 202 | 215 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `9` | `9` | 225 | START | 225 | 251 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `22` | 236 | START | 247 | 265 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 251 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_SnapReceive` | 202 | 215 | 14 | inferred_complete_timeline |
| `Action_None` | 216 | 389 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 14–386
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 279 | 78 | inferred_complete_timeline |
| `Action_None` | 283 | 386 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 302 | 101 | inferred_complete_timeline |
| `Action_None` | 304 | 389 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 276 | 75 | inferred_complete_timeline |
| `Action_None` | 284 | 289 | 6 | inferred_complete_timeline |
| `Action_None` | 291 | 389 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–368
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 203 | 190 | inferred_complete_timeline |
| `Action_SplitBlock` | 204 | 251 | 48 | inferred_complete_timeline |
| `Action_None` | 252 | 368 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 204 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 224 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 225 | 251 | 27 | inferred_complete_timeline |
| `Action_None` | 252 | 389 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 204 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 251 | 47 | inferred_complete_timeline |
| `Action_None` | 252 | 389 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–332
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_BallSnap` | 202 | 215 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 251 | 36 | inferred_complete_timeline |
| `Action_None` | 252 | 262 | 11 | inferred_complete_timeline |
| `Action_None` | 265 | 316 | 52 | inferred_complete_timeline |
| `Action_None` | 320 | 323 | 4 | inferred_complete_timeline |
| `Action_None` | 325 | 332 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 14–380
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 204 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 251 | 47 | inferred_complete_timeline |
| `Action_None` | 252 | 325 | 74 | inferred_complete_timeline |
| `Action_None` | 332 | 380 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 14–285
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 204 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 251 | 47 | inferred_complete_timeline |
| `Action_None` | 252 | 265 | 14 | inferred_complete_timeline |
| `Action_None` | 272 | 285 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 14–238
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 238 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–379
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 229 | 28 | inferred_complete_timeline |
| `Action_None` | 231 | 261 | 31 | inferred_complete_timeline |
| `Action_None` | 265 | 270 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_None` | 299 | 379 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–308
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 276 | 75 | inferred_complete_timeline |
| `Action_None` | 305 | 308 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 250 | 49 | inferred_complete_timeline |
| `Action_None` | 259 | 389 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 312 | 111 | inferred_complete_timeline |
| `Action_None` | 320 | 389 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–388
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 388 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 14–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 201 | 188 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 247–389 | 138 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 280–389 | 110 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 281–336 | 53 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 320–353 | 24 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 334–389 | 54 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 348–349 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 349–389 | 29 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 382–389 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 205 != Inferred start 216
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF3` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [202–215], lower_priority='Action_ZoneBlock' annotated_start=205, effective_Action_ZoneBlock_start=216.
- ⚠️ Action 'Action_None' range [202-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-302] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-379] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-368] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-276] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-312] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-388] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-380] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-276] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-316] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-279] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-386] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-265] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-330] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-353] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-362] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '30' has 1 frames without a visible bounding box.
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