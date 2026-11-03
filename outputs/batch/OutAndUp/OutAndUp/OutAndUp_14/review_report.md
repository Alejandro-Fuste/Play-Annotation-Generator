# Play-Annotation-Generator Annotation Review — OutAndUp_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_SellOut` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_RunGoRoute` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `16` | `15` | 27 | START | 27 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `13` | `13` | 30 | START | 30 | 34 |
| ✅ EXACT | `Action_PassBlock` | C | `2` | `2` | 30 | START | 30 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 30 | START | 30 | 58 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `7` | 30 | START | 30 | 138 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 41 | END | 27 | 41 |
| ✅ EXACT | `Action_PumpFake` | QB | `1` | `1` | 78 | START | 78 | 112 |
| ✅ EXACT | `Action_SellOut` | RG | `13` | `13` | 78 | START | 78 | 101 |
| ✅ EXACT | `Action_RunGoRoute` | RG | `13` | `13` | 102 | START | 102 | 171 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 113 | START | 113 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 41 | 15 | inferred_complete_timeline |
| `Action_None` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_PumpFake` | 78 | 112 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 166 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 51 | 25 | inferred_complete_timeline |
| `Action_None` | 53 | 116 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 58 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 140 | 79 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 157 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 54 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_SellOut` | 78 | 101 | 24 | inferred_complete_timeline |
| `Action_RunGoRoute` | 102 | 171 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 138 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 164 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 53 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 117 | 91 | inferred_complete_timeline |
| `Action_None` | 119 | 145 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 129 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 90 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 40 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–139 | 124 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 7–87 | 81 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 13–155 | 135 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 45–166 | 111 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 86–144 | 45 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 162–210 | 45 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 164–168 | 5 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 166–174 | 9 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 172–210 | 36 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 172–210 | 35 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 17: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 18: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [27-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-54] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-90] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-140] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [78-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [102-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 27, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [27-87] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [40-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>