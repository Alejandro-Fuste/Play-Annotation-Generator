# Play-Annotation-Generator Annotation Review — OutsideZoneRead_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_116`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 11 | START | 11 | 25 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 14 | START | 14 | 61 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 14 | START | 26 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 14 | START | 14 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 14 | START | 14 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `9` | 29 | START | 29 | 31 |
| ✅ EXACT | `Action_Keep` | QB | `10` | `9` | 32 | START | 32 | 46 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `9` | 47 | START | 47 | 159 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 61 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 29 | 31 | 3 | inferred_complete_timeline |
| `Action_Keep` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 159 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 88 | 78 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 132 | 151 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 61 | 48 | inferred_complete_timeline |
| `Action_None` | 62 | 77 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 61 | 36 | inferred_complete_timeline |
| `Action_None` | 62 | 98 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 61 | 48 | inferred_complete_timeline |
| `Action_None` | 62 | 180 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 61 | 48 | inferred_complete_timeline |
| `Action_None` | 62 | 180 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 94 | 84 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 90 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 104 | 94 | inferred_complete_timeline |
| `Action_None` | 106 | 130 | 25 | inferred_complete_timeline |
| `Action_None` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 131 | 121 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 180 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 135 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 29 | 19 | inferred_complete_timeline |
| `Action_None` | 31 | 174 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 130 | 120 | inferred_complete_timeline |
| `Action_None` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–180 | 180 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–124 | 121 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 22–29 | 8 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 50–180 | 131 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 58–180 | 123 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 77–159 | 79 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 102–180 | 79 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 104–180 | 77 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 107–180 | 74 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 111–179 | 57 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 134–138 | 4 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 14 != Inferred start 26

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 234: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=26.
- ⚠️ Action 'Action_None' range [11-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-27] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-90] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-151] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-94] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-163] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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