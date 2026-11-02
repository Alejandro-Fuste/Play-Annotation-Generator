# Play-Annotation-Generator Annotation Review — JetSweep_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `13` | `12` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `3` | `2` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `13` | `12` | 14 | START | 14 | 37 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `14` | `13` | 14 | END | 32 | 32 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `16` | `15` | 20 | START | 37 | 37 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 22 | START | 22 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 22 | START | 22 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 22 | START | 22 | 35 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 22 | START | 38 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 22 | START | 22 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 22 | START | 22 | 49 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 37 | START | 37 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `13` | `12` | 43 | START | 43 | 44 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `11` | `10` | 49 | BOUNDARY | 39 | 49 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `11` | `10` | 49 | BOUNDARY | 39 | 49 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `16` | `15` | 49 | BOUNDARY | 38 | 49 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `3` | `2` | 49 | BOUNDARY | 22 | 49 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `6` | `5` | 49 | BOUNDARY | 22 | 49 |

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
- **Visible Frames:** 32–78
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_Toss` | 37 | 42 | 6 | inferred_complete_timeline |
| `Action_None` | 43 | 72 | 30 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 36–77
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 53 | 77 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 14 | 37 | 24 | inferred_complete_timeline |
| `Action_JetMotion` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 180 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_LeadBlock` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_None` | 62 | 153 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 37–73
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 49 | 12 | inferred_complete_timeline |
| `Action_None` | 50 | 73 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 49 | 28 | inferred_complete_timeline |
| `Action_None` | 50 | 74 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 49 | 28 | inferred_complete_timeline |
| `Action_None` | 50 | 65 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 26 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_None` | 55 | 86 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 35 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 49 | 11 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 63 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 72 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 40 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 13–122 | 110 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 42–118 | 77 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 63–180 | 116 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 72–77 | 6 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 74–180 | 104 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 80–111 | 32 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 126–144 | 17 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 132–180 | 23 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 158–180 | 23 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 158–167 | 10 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 167–176 | 6 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `13` (2 segments found)
- ⚠️ `Action_BallSnap` for actor_track_id `16` (C): Annotated start 20 != Inferred start 37
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 22 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '13' has invalid range: start=32, end=14. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=37, end=14. Clamping end to start.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [37–37], lower_priority='Action_ZoneBlock' annotated_start=37, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [20-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-70] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [22-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-26] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-48] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [14-37] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [43-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-180] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-118] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-140] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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