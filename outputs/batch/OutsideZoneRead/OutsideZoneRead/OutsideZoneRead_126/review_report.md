# Play-Annotation-Generator Annotation Review — OutsideZoneRead_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_126`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 1
- **Action Segments:** 62
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 25 | START | 25 | 35 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 28 | START | 28 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 28 | START | 28 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 28 | START | 28 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 28 | START | 28 | 88 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `7` | 28 | START | 36 | 99 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 35 | END | 25 | 35 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `3` | `2` | 41 | START | 41 | 48 |
| ✅ EXACT | `Action_Keep` | QB | `3` | `2` | 49 | START | 49 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `3` | `2` | 64 | START | 64 | 129 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_Keep` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 129 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 155 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 55 | 31 | inferred_complete_timeline |
| `Action_None` | 59 | 113 | 55 | inferred_complete_timeline |
| `Action_None` | 115 | 138 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 99 | 72 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 88 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 99 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 180 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 99 | 72 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 99 | 72 | inferred_complete_timeline |
| `Action_None` | 100 | 132 | 33 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 33 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_None` | 41 | 63 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 30 | 6 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 140 | 116 | inferred_complete_timeline |
| `Action_None` | 149 | 180 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 51 | 27 | inferred_complete_timeline |
| `Action_None` | 55 | 82 | 28 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 180 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 146 | 122 | inferred_complete_timeline |
| `Action_None` | 148 | 180 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–149 | 150 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–114 | 46 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 72–149 | 57 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 94–180 | 87 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 103–139 | 37 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 104–180 | 77 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 111–180 | 70 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 164–179 | 16 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | 83 | 83 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 28 != Inferred start 36
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [25–35], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=36.
- ⚠️ Action 'Action_None' range [25-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-113] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 100, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [100-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-99] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-51] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-92] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>