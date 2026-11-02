# Play-Annotation-Generator Annotation Review — JetSweep_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_193`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `9` | `8` | 11 | START | 11 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 23 | START | 23 | 32 |
| ✅ EXACT | `Action_LeadBlock` | TE | `15` | `14` | 24 | START | 24 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 24 | START | 24 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 24 | START | 24 | 89 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `17` | 24 | START | 33 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 24 | START | 24 | 37 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 24 | START | 24 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 32 | END | 23 | 32 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 37 | START | 37 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `9` | `8` | 41 | START | 41 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_Toss` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_None` | 41 | 120 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_JetMotion` | 11 | 40 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 41 | 168 | 128 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_LeadBlock` | 24 | 89 | 66 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 89 | 66 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 37 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 89 | 49 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 89 | 57 | inferred_complete_timeline |
| `Action_None` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 173 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 89 | 66 | inferred_complete_timeline |
| `Action_None` | 90 | 173 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 89 | 66 | inferred_complete_timeline |
| `Action_None` | 90 | 158 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 68 | 46 | inferred_complete_timeline |
| `Action_None` | 71 | 77 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 48 | 26 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 94 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 180 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 93–100 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 94–180 | 87 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 105–159 | 55 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 111–180 | 40 | 11 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 119–121 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 24 != Inferred start 33
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 388: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [23–32], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=33.
- ⚠️ Action 'Action_None' range [23-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [41-168] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-159] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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