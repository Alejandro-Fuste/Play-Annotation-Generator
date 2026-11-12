# Play-Annotation-Generator Annotation Review — SplitZone_301

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_301`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 61 | START | 61 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `11` | `11` | 65 | START | 65 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 71 | START | 71 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 71 | START | 71 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 71 | START | 71 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 71 | START | 71 | 112 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `8` | 71 | START | 74 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 73 | END | 61 | 73 |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | Position_Unknown | `18` | `16` | 82 | START | 137 | 137 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `7` | `7` | 86 | START | 86 | 125 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 92 | START | 92 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `13` | `13` | 107 | START | 107 | 277 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 60 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_None` | 74 | 91 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 102 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SplitBlock` | 65 | 95 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 101 | 125 | 25 | inferred_complete_timeline |
| `Action_None` | 126 | 144 | 19 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 138 | 68 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 138 | 54 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 134 | 61 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 299 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 106 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 277 | 171 | inferred_complete_timeline |
| `Action_BallCarry` | 281 | 296 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 112 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 138 | 24 | inferred_complete_timeline |
| `Action_None` | 139 | 202 | 64 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 85 | 50 | inferred_complete_timeline |
| `Action_PressEdge` | 86 | 125 | 40 | inferred_complete_timeline |
| `Action_None` | 126 | 143 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 299 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 142 | 82 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 103 | 43 | inferred_complete_timeline |
| `Action_None` | 106 | 192 | 87 | inferred_complete_timeline |
| `Action_None` | 197 | 291 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 133 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 299 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 229 | 169 | inferred_complete_timeline |
| `Action_None` | 233 | 242 | 10 | inferred_complete_timeline |
| `Action_None` | 244 | 277 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 15–287 | 273 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 86–299 | 207 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 137–156 | 20 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 155–299 | 138 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 166–298 | 126 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 178–233 | 56 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 181–299 | 117 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 196–282 | 86 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 201–207 | 7 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 248–299 | 52 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 71 != Inferred start 74
- ⚠️ `Action_ReadEdgeDefender` for actor_track_id `18` (Position_Unknown): Annotated start 82 != Inferred start 137
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
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

- ⚠️ Row 604: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [61–73], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=74.
- ⚠️ Segment 'Action_ReadEdgeDefender' for track '16' has invalid range: start=137, end=91. Clamping end to start.
- ⚠️ Action 'Action_None' range [61-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-242] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-277] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-192] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-291] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-142] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [92-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [65-95] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-81] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-277] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-296] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-287] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-279] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '26' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>