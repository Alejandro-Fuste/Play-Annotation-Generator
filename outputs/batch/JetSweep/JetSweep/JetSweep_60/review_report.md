# Play-Annotation-Generator Annotation Review — JetSweep_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_60`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `23` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `16` | `15` | 33 | START | 33 | 80 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 57 | START | 57 | 62 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 62 | START | 62 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 62 | END | 57 | 62 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 62 | START | 63 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 62 | START | 62 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 62 | START | 62 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 62 | START | 62 | 77 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 72 | START | 72 | 80 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `16` | `15` | 81 | START | 81 | 272 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `24` | `23` | 82 | START | 82 | 108 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 63 | 71 | 9 | inferred_complete_timeline |
| `Action_Toss` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_None` | 81 | 209 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_LeadBlock` | 62 | 108 | 47 | inferred_complete_timeline |
| `Action_None` | 109 | 140 | 32 | inferred_complete_timeline |
| `Action_None` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_JetMotion` | 33 | 80 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 272 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 167 | 111 | inferred_complete_timeline |
| `Action_None` | 169 | 236 | 68 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 251 | 260 | 10 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |
| `Action_None` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 118 | 62 | inferred_complete_timeline |
| `Action_None` | 120 | 140 | 21 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 243 | 97 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 303 | 38 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 109 | 266 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 108 | 47 | inferred_complete_timeline |
| `Action_None` | 109 | 251 | 143 | inferred_complete_timeline |
| `Action_None` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_None` | 109 | 329 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 243 | 187 | inferred_complete_timeline |
| `Action_None` | 272 | 281 | 10 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 90 | 329 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 215 | 159 | inferred_complete_timeline |
| `Action_None` | 217 | 329 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 125 | 69 | inferred_complete_timeline |
| `Action_None` | 127 | 287 | 161 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 199 | 143 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 289 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 249 | 193 | inferred_complete_timeline |
| `Action_None` | 255 | 329 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 78 | 22 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–306 | 307 | 2 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–75 | 76 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–201 | 202 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 56–329 | 241 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 77–329 | 253 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 90–329 | 237 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 187–190 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 232–245 | 14 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 238–329 | 92 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 300–329 | 29 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 319–325 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 62 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 122: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ Row 122: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [57–62], lower_priority='Action_ZoneBlock' annotated_start=62, effective_Action_ZoneBlock_start=63.
- ⚠️ Action 'Action_None' range [57-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-167] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-243] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-303] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-289] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-329] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-251] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-287] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-81] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-293] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-287] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-308] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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