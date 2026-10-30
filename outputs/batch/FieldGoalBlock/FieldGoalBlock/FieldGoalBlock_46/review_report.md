# Play-Annotation-Generator Annotation Review — FieldGoalBlock_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_46`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `9` | `Group` | 0 | START | 0 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `11` | `11` | 7 | START | 7 | 18 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 24 | START | 24 | 35 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 49 | START | 49 | 54 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `13` | `13` | 52 | START | 52 | 62 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PlaceBall` | 24 | 35 | 12 | inferred_complete_timeline |
| `Action_None` | 36 | 90 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_None` | 55 | 90 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 21 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_None` | 38 | 59 | 22 | inferred_complete_timeline |
| `Action_None` | 63 | 90 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 90 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 7 | 18 | 12 | inferred_complete_timeline |
| `Action_LongSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_None` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 90 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 40 | 34 | inferred_complete_timeline |
| `Action_None` | 42 | 90 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 27 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–90 | 86 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–87 | 84 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–90 | 82 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–90 | 85 | 6 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–90 | 91 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–72 | 66 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 5–90 | 40 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 15–90 | 61 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 16–53 | 26 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 39–47 | 4 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 53–90 | 37 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 72–90 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_End` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 93: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [7-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-83] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [7-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-43] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-90] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-59] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-72] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-40] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-90] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>