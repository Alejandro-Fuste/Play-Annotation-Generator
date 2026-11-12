# Play-Annotation-Generator Annotation Review — SplitZone_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_90`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `0` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 17 | START | 18 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 17 | START | 18 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 17 | START | 18 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 17 | START | 18 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 17 | START | 51 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 17 | START | 18 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 17 | START | 18 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 17 | START | 18 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 17 | START | 18 | 192 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `17` | `17` | 190 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 193 | START | 193 | 257 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `17` | `17` | 193 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 193 | START | 193 | 325 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 193 | START | 193 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `8` | 193 | START | 193 | 220 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 198 | END | 190 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `0` | `0` | 200 | START | 200 | 232 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 207 | START | 207 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 229 | START | 229 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `6` | `6` | 229 | START | 229 | 295 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 325 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 18–311
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 206 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 228 | 22 | inferred_complete_timeline |
| `Action_None` | 229 | 253 | 25 | inferred_complete_timeline |
| `Action_None` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 311 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–507
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 228 | 211 | inferred_complete_timeline |
| `Action_BallCarry` | 229 | 311 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 314 | 477 | 164 | inferred_complete_timeline |
| `Action_BallCarry` | 489 | 500 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 502 | 504 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 506 | 507 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–207
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 207 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 18–307
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 199 | 182 | inferred_complete_timeline |
| `Action_SplitBlock` | 200 | 232 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 254 | 307 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 192 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 228 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 229 | 295 | 67 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 297 | 325 | 29 | inferred_complete_timeline |
| `Action_None` | 326 | 509 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 192 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 325 | 133 | inferred_complete_timeline |
| `Action_None` | 326 | 356 | 31 | inferred_complete_timeline |
| `Action_None` | 386 | 509 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 51–130
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 124 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–301
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 192 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 220 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 222 | 301 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–278
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 192 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 257 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 259 | 278 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 250 | 61 | inferred_complete_timeline |
| `Action_None` | 252 | 509 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–376
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 376 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 18–338
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 31 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 189 | 151 | inferred_complete_timeline |
| `Action_None` | 190 | 207 | 18 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 338 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 18–268
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 60 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 196 | 222 | 27 | inferred_complete_timeline |
| `Action_None` | 229 | 264 | 36 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 18–475
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 307 | 118 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 475 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–220
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 220 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–246
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_None` | 190 | 246 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–49
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 49 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–249
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 140 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 249 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 147–252 | 106 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 197–335 | 138 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 206–261 | 56 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 217–340 | 124 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 231–298 | 68 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 236–285 | 47 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 255–343 | 76 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 258–268 | 11 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 265–286 | 20 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 270–297 | 23 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 271–315 | 36 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 273–314 | 12 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 275–509 | 207 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 301–350 | 44 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 324–509 | 184 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 326–509 | 160 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 341–345 | 5 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 343–509 | 167 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 345–414 | 37 | 5 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 374–502 | 109 | 5 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 380–382 | 3 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 391–393 | 3 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 401–486 | 86 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 405–509 | 100 | 3 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 420–498 | 77 | 2 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 427–509 | 83 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 449–458 | 10 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 496–500 | 5 | 1 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 509–509 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LG) duration 133 frames exceeds threshold 90 frames [start=193, end=325].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '6' (LT) duration 97 frames exceeds threshold 90 frames [start=229, end=325].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 109 frames exceeds threshold 90 frames [start=193, end=301].
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=190, end=130. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=193, end=130. Clamping end to start.
- ⚠️ Action 'Action_SplitBlock' range [200-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [254-307] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [259-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [314-477] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [489-500] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [502-504] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [506-507] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-246] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-356] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-49] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [229-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [297-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-509] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [222-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-376] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-253] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-307] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-475] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-338] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-335] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-340] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-272] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-306] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-500] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-330] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-350] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-369] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-372] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-484] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-360] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-397] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-392] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-467] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-490] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-498] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-486] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-462] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-497] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-492] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-498] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-458] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '46' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.

</details>