# Play-Annotation-Generator Annotation Review — JetSweep_206

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_206`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 34
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `18` |
| ⚠️ START CHANGED | `Action_LeadBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 59 | START | 59 | 73 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `20` | `18` | 60 | START | 60 | 88 |
| ⚠️ START CHANGED | `Action_LeadBlock` | C | `8` | `7` | 63 | START | 74 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 63 | START | 63 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 63 | START | 63 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 63 | START | 63 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 63 | START | 63 | 119 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `8` | `7` | 63 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 73 | END | 59 | 73 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 83 | START | 83 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `18` | 89 | START | 89 | 228 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_None` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_Toss` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 124 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 199 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 93 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 119 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 141 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_LeadBlock` | 74 | 97 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 116 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 151 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 184 | 21 | inferred_complete_timeline |
| `Action_None` | 185 | 219 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 101 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 58 | 35 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 239 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 148 | 90 | inferred_complete_timeline |
| `Action_None` | 163 | 230 | 68 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–142 | 49 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–239 | 237 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 53–112 | 60 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 60–239 | 176 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 82–148 | 57 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 105–239 | 135 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 113–239 | 125 | 2 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_LeadBlock` for actor_track_id `8` (C): Annotated start 63 != Inferred start 74
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 414: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 122 frames exceeds threshold 90 frames [start=63, end=184].
- ⚠️ Overlapping action conflict at frame 63 for track '7': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [59–73], lower_priority='Action_LeadBlock' annotated_start=63, effective_Action_LeadBlock_start=74.
- ⚠️ Action 'Action_None' range [59-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-116] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-151] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [74-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-101] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-230] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-228] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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