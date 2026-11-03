# Play-Annotation-Generator Annotation Review — Slants0to10_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_53`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 3 | START | 3 | 17 |
| ✅ EXACT | `Action_PassBlock` | LT | `14` | `14` | 7 | START | 7 | 202 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `17` | `17` | 7 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 7 | START | 7 | 8 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 7 | START | 7 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 7 | START | 7 | 14 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `17` | `17` | 18 | END | N/A | N/A |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `1` | `1` | 22 | START | 22 | 65 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 57 | START | 57 | 65 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 114 | START | 114 | 119 |

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
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_None` | 66 | 102 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 65 | 63 | inferred_complete_timeline |
| `Action_None` | 75 | 113 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 280 | 278 | inferred_complete_timeline |
| `Action_None` | 307 | 319 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 22 | 65 | 44 | inferred_complete_timeline |
| `Action_None` | 66 | 113 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 119 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 387 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 290 | 288 | inferred_complete_timeline |
| `Action_None` | 292 | 419 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 202 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 35 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 57 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_None` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 290 | 250 | inferred_complete_timeline |
| `Action_None` | 292 | 323 | 32 | inferred_complete_timeline |
| `Action_None` | 329 | 337 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 14 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 38 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 78 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 89 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 213 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 104 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 321 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_None` | 127 | 173 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 419 | 417 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 122 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 58 | 56 | inferred_complete_timeline |
| `Action_None` | 73 | 127 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_None` | 95 | 214 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 277 | 275 | inferred_complete_timeline |
| `Action_None` | 282 | 349 | 68 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_None` | 360 | 361 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 113 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 292 | 290 | inferred_complete_timeline |
| `Action_None` | 294 | 393 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–408
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 408 | 406 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 38–136 | 79 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 54–97 | 44 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 117–333 | 210 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 132–419 | 284 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 150–173 | 24 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 152–419 | 268 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 164–169 | 6 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 249–251 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 317–319 | 3 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 322–419 | 91 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 333–419 | 86 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 336–419 | 84 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 346–419 | 74 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 357–419 | 63 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 362–419 | 58 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 364–419 | 56 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 414–419 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '17' has invalid range: start=7, end=2. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=19.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_SnapReceive' annotated_start=3, effective_Action_SnapReceive_start=19.
- ⚠️ Action 'Action_None' range [3-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-214] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-408] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-292] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-393] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-349] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-321] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-280] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-122] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-290] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-419] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-111] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [3-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-31] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-290] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-323] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-8] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-57] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-136] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-280] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-404] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-387] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-352] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>