# Play-Annotation-Generator Annotation Review — SplitZone_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_126`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 60
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 31 | START | 31 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 34 | START | 48 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 34 | START | 34 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 34 | START | 34 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 34 | START | 34 | 102 |
| ✅ EXACT | `Action_SplitBlock` | HB | `10` | `10` | 41 | START | 41 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 47 | END | 31 | 47 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `3` | 51 | START | 51 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 57 | START | 57 | 66 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_None` | 57 | 127 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 119 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 123 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SplitBlock` | 41 | 153 | 113 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 145 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 102 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 153 | 50 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 111 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 153 | 120 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 172 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_None` | 54 | 82 | 29 | inferred_complete_timeline |
| `Action_None` | 90 | 132 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 55–180 | 121 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 100–174 | 52 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 126–180 | 55 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 144–180 | 37 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 145–180 | 32 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 254: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 118 frames exceeds threshold 90 frames [start=34, end=151].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 120 frames exceeds threshold 90 frames [start=34, end=153].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [31–47], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=48.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 120 frames exceeds threshold 90 frames [start=34, end=153].
- ⚠️ Action 'Action_None' range [31-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-145] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-49] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-82] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>