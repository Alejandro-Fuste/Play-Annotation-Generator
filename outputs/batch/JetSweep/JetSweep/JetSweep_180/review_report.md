# Play-Annotation-Generator Annotation Review — JetSweep_180

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_180`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | offense | `17` | `15` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `7` | `6` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `5` | `4` |
| ✅ EXACT | `Action_Toss` | Position_Unknown | Team_Unknown | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `17` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 36 |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | `17` | `15` | 23 | START | 24 | 63 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `7` | `6` | 36 | START | 36 | 51 |
| ✅ EXACT | `Action_LeadBlock` | TE | `14` | `13` | 37 | START | 37 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 37 | START | 37 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 37 | START | 37 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 37 | START | 37 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 37 | START | 37 | 79 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `5` | `4` | 51 | END | 36 | 51 |
| ✅ EXACT | `Action_Toss` | Position_Unknown | `5` | `4` | 59 | START | 59 | 63 |
| ✅ EXACT | `Action_BallCarry` | WR | `17` | `15` | 64 | START | 64 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 97 | 62 | inferred_complete_timeline |
| `Action_None` | 107 | 126 | 20 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 24–110
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 24 | 63 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 110 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 36 | 32 | inferred_complete_timeline |
| `Action_LeadBlock` | 37 | 117 | 81 | inferred_complete_timeline |
| `Action_None` | 118 | 148 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 67 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 73 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 55 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 79 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 107 | 56 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 136 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 78 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 51 | 16 | inferred_complete_timeline |
| `Action_None` | 52 | 83 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 36 | 81 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 55 | 20 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 139 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_None` | 36 | 82 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–82 | 81 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–269 | 218 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 42–86 | 45 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 59–80 | 22 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 66–87 | 22 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 82–108 | 25 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 87–250 | 163 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 119–220 | 102 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 127–141 | 15 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 142–156 | 15 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 155–269 | 111 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 170–269 | 72 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 224–269 | 45 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 258–267 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `17` (WR): Annotated start 23 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 362: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 362: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [36-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [59-63] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-50] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-97] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-126] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-81] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [37-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [24-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-87] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-267] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>