# Play-Annotation-Generator Annotation Review — Post10to15_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_61`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 120
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_RunPostRoute` | SAF | defense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 8 | START | 8 | 21 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `11` | 11 | START | 22 | 78 |
| ✅ EXACT | `Action_PassBlock` | RG | `13` | `13` | 11 | START | 11 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 11 | START | 11 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 11 | START | 11 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 11 | START | 11 | 117 |
| ✅ EXACT | `Action_RunPostRoute` | SAF | `0` | `0` | 21 | START | 21 | 56 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 21 | END | 8 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `21` | `21` | 77 | START | 77 | 80 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 22 | 76 | 55 | inferred_complete_timeline |
| `Action_ThrowPass` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 122 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 73 | 66 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 156 | 35 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 77 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 103 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 113 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 70 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 180 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 78 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 111 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 98 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 54 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 161 | 154 | inferred_complete_timeline |
| `Action_None` | 165 | 178 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 78 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 120 | 113 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_None` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 59 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunPostRoute` | 21 | 56 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 17–111 | 39 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 57–77 | 21 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 58–180 | 116 | 5 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 58–78 | 21 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 79–149 | 61 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 79–162 | 84 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 79–98 | 18 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 98–179 | 78 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 112–180 | 69 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 112–173 | 45 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 116–180 | 55 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 124–180 | 43 | 5 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 136–155 | 18 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 166–180 | 14 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 11 != Inferred start 22
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [8–21], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=22.
- ⚠️ Action 'Action_RunPostRoute' range [21-56] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-101] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-120] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-122] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [77-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-119] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-130] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-162] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-173] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>