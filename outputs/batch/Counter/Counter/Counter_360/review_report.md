# Play-Annotation-Generator Annotation Review — Counter_360

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_360`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 53
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 0
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 4
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `35` | `14` |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | offense | `11` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `34` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `35` | `14` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF1 | defense | `1` | `0` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `33` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF1 | defense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 19 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 29 | 31 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `35` | `14` | 32 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | `11` | `9` | 37 | START | 55 | 68 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `34` | `13` | 37 | START | 190 | 190 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `35` | `14` | 37 | START | 190 | 190 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | `6` | `5` | 37 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF1 | `1` | `0` | 37 | START | 37 | 46 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `33` | `12` | 50 | END | 190 | 190 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF1 | `1` | `0` | 76 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 83 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 29–68
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 31 | 3 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–23
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 23 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 55–68
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 55 | 68 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 31–68
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–68
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 31 | 24 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 68 | 37 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 48 | 68 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 9 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 31 | 21 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `31` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `11` | `32` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `12` | `33` | Position_Unknown | Team_Unknown | 190–210 | 21 | 2 | Undefined position; Undefined team |
| `13` | `34` | Position_Unknown | Team_Unknown | 190–210 | 21 | 2 | Undefined position; Undefined team |
| `14` | `35` | Position_Unknown | Team_Unknown | 190–210 | 21 | 2 | Undefined position; Undefined team |
| `15` | `36` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `16` | `37` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `17` | `38` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `18` | `39` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `19` | `40` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `20` | `41` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `21` | `42` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `22` | `43` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `23` | `44` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `24` | `45` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `25` | `46` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `26` | `47` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `27` | `48` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `28` | `49` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `29` | `50` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (Position_Unknown)
- ⚠️ `Action_DownBlock` for actor_track_id `11` (RT): Annotated start 37 != Inferred start 55
- ⚠️ `Action_DownBlock` for actor_track_id `34` (Position_Unknown): Annotated start 37 != Inferred start 190
- ⚠️ `Action_DownBlock` for actor_track_id `35` (Position_Unknown): Annotated start 37 != Inferred start 190
- ❌ Missing segment for action `Action_PullBlock` on target `6` (LG)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `0` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `0` (SAF1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 13 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 722: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 722: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Track ID '12' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '10' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '13' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=76, end=68. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '5' has invalid range: start=37, end=23. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '12' has invalid range: start=190, end=50. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '13' has invalid range: start=190, end=83. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=190, end=50. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=190, end=83. Clamping end to start.
- ⚠️ Action 'Action_PullLeadBlock' range [37-46] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-9] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>