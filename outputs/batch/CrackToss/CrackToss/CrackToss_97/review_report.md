# Play-Annotation-Generator Annotation Review — CrackToss_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_97`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_PullBlock` | RB2 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 37 | START | 37 | 41 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `21` | `19` | 40 | START | 40 | 129 |
| ✅ EXACT | `Action_PullBlock` | RB2 | `11` | `10` | 40 | START | 40 | 132 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 41 | END | 37 | 41 |
| ❌ MISSING SEGMENT | `Action_Toss` | QB | `16` | `15` | 48 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `5` | `4` | 70 | START | 70 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 139 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PullBlock` | 40 | 132 | 93 | inferred_complete_timeline |
| `Action_None` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 156 | 120 | inferred_complete_timeline |
| `Action_None` | 159 | 175 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 101 | 28 | inferred_complete_timeline |
| `Action_None` | 104 | 127 | 24 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 175 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 174 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 175 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 64 | 28 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 175 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 175 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 164 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 172 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 175 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 175 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–134 | 133 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–142 | 140 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 8–175 | 168 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 22–47 | 21 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 38–175 | 123 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 47–96 | 50 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 55–74 | 20 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 74–175 | 100 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 86–175 | 85 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 132–175 | 35 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 138–175 | 38 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 161–175 | 15 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 165–175 | 11 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_Toss` on target `16` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 196: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (RB2) duration 93 frames exceeds threshold 90 frames [start=40, end=132].
- ⚠️ Segment 'Action_Toss' for track '15' has invalid range: start=48, end=47. Clamping end to start.
- ⚠️ Action 'Action_None' range [37-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-139] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-142] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-156] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [40-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-174] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-134] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [42-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [40-129] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-175] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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