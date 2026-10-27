# Play-Annotation-Generator Annotation Review — Counter_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 35
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `13` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 50 | START | 50 | 103 |
| ✅ EXACT | `Action_DownBlock` | RG | `10` | `9` | 103 | START | 103 | 171 |
| ✅ EXACT | `Action_DownBlock` | LG | `22` | `21` | 103 | START | 103 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | `9` | `8` | 103 | START | 103 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `21` | `20` | 103 | START | 104 | 131 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `18` | `17` | 103 | START | 103 | 171 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 103 | END | 50 | 103 |
| ✅ EXACT | `Action_BallCarry` | QB | `20` | `19` | 134 | START | 134 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 171 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 103 | 54 | inferred_complete_timeline |
| `Action_None` | 104 | 133 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 227 | 178 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 233 | 184 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 171 | 69 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 50 | 103 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 131 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 134 | 171 | 38 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 171 | 69 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 103 | 171 | 69 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 209 | 160 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 135 | 86 | inferred_complete_timeline |
| `Action_None` | 150 | 228 | 79 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 185 | 136 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 233 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 171 | 69 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 130–141 | 9 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 190–192 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 18 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [50–103], lower_priority='Action_PullBlock' annotated_start=103, effective_Action_PullBlock_start=104.
- ⚠️ Action 'Action_None' range [50-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-228] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>