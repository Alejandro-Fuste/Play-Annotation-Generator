# Play-Annotation-Generator Annotation Review — JetSweep_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `10` | `9` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_JetMotion` | WR | `10` | `9` | 6 | START | 6 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 19 | START | 19 | 34 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 22 | START | 22 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 22 | START | 22 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 22 | START | 22 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 22 | START | 35 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 22 | START | 22 | 35 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 34 | END | 19 | 34 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 42 | START | 42 | 51 |
| ✅ EXACT | `Action_BallCarry` | WR | `10` | `9` | 52 | START | 52 | 180 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `16` | `15` | 54 | START | 54 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `14` | `13` | 70 | BOUNDARY | 57 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `20` | `19` | 70 | BOUNDARY | 22 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `21` | `20` | 70 | BOUNDARY | 53 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `22` | `21` | 70 | BOUNDARY | 41 | 70 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_None` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_Toss` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_None` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_LeadBlock` | 22 | 70 | 49 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_JetMotion` | 6 | 51 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 37 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 70 | 30 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 70 | 49 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 69 | 51 | inferred_complete_timeline |
| `Action_None` | 74 | 150 | 77 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 48 | 30 | inferred_complete_timeline |
| `Action_None` | 51 | 180 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 172 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 124 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 71 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 180 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–180 | 181 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 52–90 | 4 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 85–180 | 94 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 95–99 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 132–180 | 49 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 157–174 | 14 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 39: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [19–34], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=35.
- ⚠️ Action 'Action_None' range [19-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-124] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-51] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>