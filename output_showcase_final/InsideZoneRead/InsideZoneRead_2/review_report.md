# Play-Annotation-Generator Annotation Review — InsideZoneRead_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 55 | START | 55 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 57 | START | 57 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 57 | START | 69 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 57 | START | 57 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 57 | START | 57 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 68 | END | 55 | 68 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `3` | 71 | START | 71 | 81 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 82 | START | 82 | 86 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 88 | START | 88 | 98 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 82 | 86 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 98 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 140 | 74 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 125 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 83 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 140 | 60 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 171 | 27 | inferred_complete_timeline |
| `Action_None` | 173 | 211 | 39 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 164 | 110 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 78 | 24 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 229 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 239 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 84 | 30 | inferred_complete_timeline |
| `Action_None` | 86 | 111 | 26 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 141 | 87 | inferred_complete_timeline |
| `Action_None` | 145 | 233 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 102 | 48 | inferred_complete_timeline |
| `Action_None` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 15–157 | 129 | 7 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 84–239 | 144 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 94–216 | 123 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 99–239 | 112 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 111–239 | 124 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 142–239 | 91 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 144–237 | 94 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 169–239 | 54 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 170–187 | 18 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 209–239 | 27 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 209–213 | 5 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 227–238 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_ZoneBlock' annotated_start=57, effective_Action_ZoneBlock_start=69.
- ⚠️ Action 'Action_None' range [55-164] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [82-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-141] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-233] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-111] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-138] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-187] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>