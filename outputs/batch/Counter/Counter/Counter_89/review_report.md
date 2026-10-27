# Play-Annotation-Generator Annotation Review — Counter_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_89`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | LB2 | defense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 118 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 119 | START | 119 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 124 | START | 124 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 124 | START | 139 | 200 |
| ✅ EXACT | `Action_DownBlock` | LG | `22` | `21` | 124 | START | 124 | 172 |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | LT | `20` | `19` | 124 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `6` | 124 | START | 124 | 157 |
| ✅ EXACT | `Action_PullLeadBlock` | LB2 | `14` | `13` | 124 | START | 124 | 200 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 138 | END | 119 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `1` | `0` | 165 | START | 165 | 201 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_None` | 139 | 288 | 150 | inferred_complete_timeline |
| `Action_None` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 240 | 122 | inferred_complete_timeline |
| `Action_None` | 244 | 253 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 359 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 208 | 90 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 273 | 155 | inferred_complete_timeline |
| `Action_None` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 133 | 15 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 135 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 172 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 238 | 38 | inferred_complete_timeline |
| `Action_None` | 240 | 359 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 172 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 200 | 62 | inferred_complete_timeline |
| `Action_None` | 201 | 359 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 157 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 201 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 359 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 159 | 41 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 359 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 157 | 39 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 331 | 213 | inferred_complete_timeline |
| `Action_None` | 338 | 344 | 7 | inferred_complete_timeline |
| `Action_None` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 166 | 48 | inferred_complete_timeline |
| `Action_None` | 170 | 359 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 229 | 111 | inferred_complete_timeline |
| `Action_None` | 231 | 248 | 18 | inferred_complete_timeline |
| `Action_None` | 255 | 359 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 124 | 200 | 77 | inferred_complete_timeline |
| `Action_None` | 201 | 260 | 60 | inferred_complete_timeline |
| `Action_None` | 262 | 359 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 359 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 276 | 158 | inferred_complete_timeline |
| `Action_None` | 283 | 291 | 9 | inferred_complete_timeline |
| `Action_None` | 295 | 329 | 35 | inferred_complete_timeline |
| `Action_None` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 359 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 193 | 75 | inferred_complete_timeline |
| `Action_None` | 200 | 315 | 116 | inferred_complete_timeline |
| `Action_None` | 329 | 333 | 5 | inferred_complete_timeline |
| `Action_None` | 335 | 339 | 5 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 304 | 186 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 158–203 | 44 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 192–359 | 155 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 196–213 | 18 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 202–285 | 69 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 208–242 | 35 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 214–333 | 104 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 220–359 | 140 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 225–359 | 132 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 227–233 | 7 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 318–331 | 7 | 2 | Undefined position; Undefined team |
| `33` | `56` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_PlaySideFakeStep` on target `20` (LT)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Overlapping action conflict at frame 124 for track '19': 'Action_PlaySideFakeStep' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [119–138], lower_priority='Action_DownBlock' annotated_start=124, effective_Action_DownBlock_start=139.
- ⚠️ Action 'Action_BallCarry' range [165-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-331] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [169-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [172-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [179-182] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-273] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-288] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [151-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-238] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-213] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-264] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-242] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '33' has 1 frames without a visible bounding box.
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

</details>