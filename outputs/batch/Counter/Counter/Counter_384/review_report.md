# Play-Annotation-Generator Annotation Review — Counter_384

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_384`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 144 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 142 | START | 142 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 145 | START | 160 | 175 |
| ✅ EXACT | `Action_DownBlock` | TE | `4` | `3` | 145 | START | 145 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 145 | START | 145 | 175 |
| ✅ EXACT | `Action_PullBlock` | LG | `5` | `4` | 145 | START | 145 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `18` | `17` | 145 | START | 145 | 211 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 159 | END | 142 | 159 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 170 | START | 170 | 186 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 187 | START | 187 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 227 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 170 | 186 | 17 | inferred_complete_timeline |
| `Action_None` | 187 | 389 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 389 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 389 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 227 | 83 | inferred_complete_timeline |
| `Action_None` | 228 | 389 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 212 | 71 | inferred_complete_timeline |
| `Action_None` | 218 | 389 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PullBlock` | 145 | 227 | 83 | inferred_complete_timeline |
| `Action_None` | 228 | 354 | 127 | inferred_complete_timeline |
| `Action_None` | 365 | 389 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_BallSnap` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 175 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 227 | 39 | inferred_complete_timeline |
| `Action_None` | 228 | 378 | 151 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 175 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 178 | 185 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 227 | 29 | inferred_complete_timeline |
| `Action_None` | 228 | 389 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 389 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 207 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 240 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 173 | 32 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 389 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 215 | 74 | inferred_complete_timeline |
| `Action_None` | 221 | 353 | 133 | inferred_complete_timeline |
| `Action_None` | 357 | 389 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 389 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 199 | 58 | inferred_complete_timeline |
| `Action_None` | 202 | 213 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 199 | 58 | inferred_complete_timeline |
| `Action_None` | 210 | 219 | 10 | inferred_complete_timeline |
| `Action_None` | 221 | 385 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 201 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 15–389 | 358 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 66–389 | 324 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 166–389 | 221 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 197–389 | 193 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 200–389 | 181 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 217–389 | 173 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 232–389 | 158 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 240–389 | 150 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 254–389 | 132 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 281–324 | 41 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 289–310 | 22 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 292–308 | 8 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 307–347 | 16 | 4 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 356–360 | 4 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 381–389 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [142–159], lower_priority='Action_DownBlock' annotated_start=145, effective_Action_DownBlock_start=160.
- ⚠️ Action 'Action_None' range [142-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-385] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-354] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [178-185] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-197] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-240] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-378] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-353] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-173] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [145-211] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-306] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-362] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-310] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '32' has 2 frames without a visible bounding box.
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

</details>