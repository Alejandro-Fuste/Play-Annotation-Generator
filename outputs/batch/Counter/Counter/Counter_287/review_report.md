# Play-Annotation-Generator Annotation Review — Counter_287

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_287`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 144 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `1` | 145 | START | 145 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 148 | START | 148 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `22` | `21` | 148 | START | 148 | 171 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 148 | START | 148 | 240 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `19` | `18` | 148 | START | 148 | 240 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 161 | END | 145 | 161 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 174 | START | 174 | 193 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 194 | START | 194 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 240 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_SnapReceive` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 193 | 20 | inferred_complete_timeline |
| `Action_None` | 194 | 214 | 21 | inferred_complete_timeline |
| `Action_None` | 216 | 321 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 359 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 340 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 245 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 286 | 142 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 171 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 240 | 54 | inferred_complete_timeline |
| `Action_None` | 241 | 345 | 105 | inferred_complete_timeline |
| `Action_None` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 167 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 240 | 69 | inferred_complete_timeline |
| `Action_None` | 241 | 359 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_BallSnap` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_None` | 162 | 359 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 240 | 93 | inferred_complete_timeline |
| `Action_None` | 241 | 323 | 83 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 148 | 240 | 93 | inferred_complete_timeline |
| `Action_None` | 241 | 359 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 267 | 123 | inferred_complete_timeline |
| `Action_None` | 274 | 276 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 172 | 28 | inferred_complete_timeline |
| `Action_None` | 181 | 200 | 20 | inferred_complete_timeline |
| `Action_None` | 206 | 257 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 245 | 101 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 207 | 63 | inferred_complete_timeline |
| `Action_None` | 210 | 226 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 358 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 241 | 97 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 359 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 245 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–298 | 299 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 232–359 | 128 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 254–359 | 106 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 275–359 | 85 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 576: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
- ⚠️ Action 'Action_None' range [145-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-340] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-226] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-323] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-298] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-286] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [148-240] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-240] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>