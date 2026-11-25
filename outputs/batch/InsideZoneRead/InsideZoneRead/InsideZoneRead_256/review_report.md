# Play-Annotation-Generator Annotation Review — InsideZoneRead_256

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_256`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 56
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_Keep` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | DT2 | defense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 0 | START | 0 | 14 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 3 | START | 3 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 3 | START | 3 | 76 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 3 | START | 15 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 3 | START | 3 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 3 | START | 3 | 76 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `15` | `14` | 14 | END | 0 | 14 |
| ✅ EXACT | `Action_ReadDefender` | DT2 | `15` | `14` | 16 | START | 16 | 19 |
| ✅ EXACT | `Action_Keep` | DT2 | `15` | `14` | 20 | START | 20 | 43 |
| ✅ EXACT | `Action_BallCarry` | DT2 | `15` | `14` | 44 | START | 44 | 95 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 66 | 148 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 134 | 58 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 76 | 62 | inferred_complete_timeline |
| `Action_None` | 77 | 128 | 52 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_None` | 113 | 132 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 121 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 103 | 127 | 25 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 36 | 51 | 16 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_Keep` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 95 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 87 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 26–125 | 29 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 76–139 | 52 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 98–180 | 83 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 99–180 | 82 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 101–180 | 68 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 155–178 | 24 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 164–180 | 17 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 169–180 | 12 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 3 != Inferred start 15

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [0–14], lower_priority='Action_ZoneBlock' annotated_start=3, effective_Action_ZoneBlock_start=15.
- ⚠️ Action 'Action_None' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-148] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-51] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-107] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_256'; source metadata written as null.

</details>