# Play-Annotation-Generator Annotation Review — Counter_263

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_263`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | DT2 | defense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `13` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 51 | START | 51 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `16` | `15` | 54 | START | 54 | 73 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `19` | `18` | 54 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `3` | 54 | START | 54 | 78 |
| ✅ EXACT | `Action_PullBlock` | DT2 | `22` | `21` | 54 | START | 54 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | `3` | `2` | 54 | START | 54 | 101 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `19` | `18` | 66 | END | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | C | `19` | `18` | 95 | START | 95 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 128 | 78 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 168 | 118 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 198 | 15 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 54 | 101 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 114 | 122 | 9 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 125 | 128 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 204 | 154 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 87 | 37 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 149 | 99 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 78 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 73 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 128 | 51 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 66 | 16 | inferred_complete_timeline |
| `Action_None` | 67 | 94 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 150 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 207 | 157 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 99 | 49 | inferred_complete_timeline |
| `Action_None` | 108 | 175 | 68 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 54 | 128 | 75 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 159 | 109 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–210 | 206 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–210 | 125 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 173–192 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `19` (C)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 528: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '18' has invalid range: start=54, end=50. Clamping end to start.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [51–66], lower_priority='Action_DownBlock' annotated_start=54, effective_Action_DownBlock_start=67.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [51–66], lower_priority='Action_SnapReceive' annotated_start=51, effective_Action_SnapReceive_start=67.
- ⚠️ Action 'Action_None' range [51-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [54-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [114-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-159] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [51-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '18' starts at frame 95, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [95-150] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [54-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>