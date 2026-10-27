# Play-Annotation-Generator Annotation Review — Dagger_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_39`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 31
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BreakInside` | LB1 | defense | `7` | `7` |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 143 | START | 143 | 152 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 147 | START | 153 | 269 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 147 | START | 147 | 266 |
| ✅ EXACT | `Action_PassBlock` | LT | `3` | `3` | 147 | START | 147 | 269 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 147 | START | 147 | 264 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 152 | END | 143 | 152 |
| ✅ EXACT | `Action_BreakInside` | LB1 | `7` | `7` | 161 | START | 161 | 250 |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | `1` | `1` | 161 | START | 161 | 220 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 210 | START | 210 | 220 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 153 | 209 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 221 | 263 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_ClearToEdge` | 161 | 220 | 60 | inferred_complete_timeline |
| `Action_None` | 221 | 263 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 269 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 266 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 264 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 264 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 255 | 113 | inferred_complete_timeline |
| `Action_None` | 259 | 266 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BreakInside` | 161 | 250 | 90 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 262 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 258 | 116 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–269 | 264 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–264 | 265 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–262 | 258 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–267 | 266 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 147 != Inferred start 153

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 18 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [143–152], lower_priority='Action_PassBlock' annotated_start=147, effective_Action_PassBlock_start=153.
- ⚠️ Action 'Action_None' range [143-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-263] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-262] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-254] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-264] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-262] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-262] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-264] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.

</details>