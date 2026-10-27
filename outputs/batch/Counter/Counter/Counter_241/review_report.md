# Play-Annotation-Generator Annotation Review — Counter_241

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_241`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 171 | START | 171 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 176 | START | 176 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `21` | `20` | 176 | START | 176 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `3` | `2` | 176 | START | 184 | 218 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `15` | `14` | 176 | START | 176 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `16` | `15` | 176 | START | 176 | 228 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `10` | `9` | 176 | START | 176 | 268 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 183 | END | 171 | 183 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 191 | START | 191 | 216 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `15` | `14` | 217 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_SnapReceive` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 191 | 216 | 26 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 176 | 207 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 176 | 268 | 93 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 175 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 262 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 175 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 200 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 228 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 268 | 25 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 218 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 268 | 46 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 228 | 53 | inferred_complete_timeline |
| `Action_PullBlock` | 232 | 245 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 249 | 268 | 20 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 170 | 157 | inferred_complete_timeline |
| `Action_None` | 171 | 237 | 67 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 170 | 129 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 249 | 79 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 233 | 63 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 261 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 211–269 | 53 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `15` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 483: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 93 frames exceeds threshold 90 frames [start=176, end=268].
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [171–183], lower_priority='Action_DownBlock' annotated_start=176, effective_Action_DownBlock_start=184.
- ⚠️ Segment 'Action_BallCarry' for track '14' has invalid range: start=217, end=207. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '15' (RG) duration 93 frames exceeds threshold 90 frames [start=176, end=268].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 93 frames exceeds threshold 90 frames [start=176, end=268].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LT) duration 93 frames exceeds threshold 90 frames [start=176, end=268].
- ⚠️ Action 'Action_None' range [171-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-218] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [176-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [176-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [232-245] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-200] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-228] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [244-268] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-262] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>