# Play-Annotation-Generator Annotation Review — JetSweep_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_25`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | defense | `6` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `2` | `1` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_JetMotion` | WR | `2` | `1` | 12 | START | 12 | 69 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 44 | START | 44 | 55 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | `6` | `5` | 53 | START | 53 | 109 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 53 | START | 56 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 53 | START | 53 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 53 | START | 53 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 53 | START | 53 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 53 | START | 53 | 71 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 55 | END | 44 | 55 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 62 | START | 62 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `2` | `1` | 70 | START | 70 | 177 |
| ✅ EXACT | `Action_LeadBlock` | RB | `7` | `6` | 79 | START | 79 | 109 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `14` | `13` | 109 | BOUNDARY | 56 | 109 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `18` | `17` | 109 | BOUNDARY | N/A | 109 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `20` | `19` | 109 | BOUNDARY | 53 | 109 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `21` | `20` | 109 | BOUNDARY | 81 | 109 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `22` | `21` | 109 | BOUNDARY | 74 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_Toss` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 70 | 165 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 109 | 31 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 105 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_JetMotion` | 12 | 69 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 177 | 108 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 208 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 97 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 71 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 109 | 36 | inferred_complete_timeline |
| `Action_None` | 110 | 140 | 31 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 66 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 81 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 109 | 54 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 67 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 109 | 29 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 109 | 57 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 72 | 29 | inferred_complete_timeline |
| `Action_None` | 74 | 210 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 84 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 53 | 109 | 57 | inferred_complete_timeline |
| `Action_None` | 110 | 197 | 88 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 78 | 35 | inferred_complete_timeline |
| `Action_None` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 108 | 65 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 175 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 130 | 87 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–202 | 103 | 8 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 86–87 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 89–210 | 122 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 112–210 | 99 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 182–209 | 13 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 53 != Inferred start 56
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [44–55], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=56.
- ⚠️ Action 'Action_None' range [44-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-197] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-105] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
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

</details>