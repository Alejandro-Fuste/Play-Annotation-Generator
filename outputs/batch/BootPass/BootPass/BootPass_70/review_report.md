# Play-Annotation-Generator Annotation Review — BootPass_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `23` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 58 | START | 58 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `0` | `0` | 68 | START | 68 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `12` | `12` | 68 | START | 68 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `4` | `4` | 68 | START | 68 | 80 |
| ✅ EXACT | `Action_RunBlock` | LT | `7` | `7` | 68 | START | 68 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `9` | `9` | 68 | START | 73 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 72 | END | 58 | 72 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `8` | `8` | 82 | START | 82 | 91 |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | `8` | `8` | 98 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `8` | `8` | 156 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `23` | `19` | 195 | START | 195 | 206 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_FakeHandoff` | 82 | 91 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 190 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 101 | 44 | inferred_complete_timeline |
| `Action_None` | 105 | 142 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 135 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 172 | 90 | inferred_complete_timeline |
| `Action_RunBlock` | 175 | 195 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 154 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 90 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 109 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 94 | 27 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 140 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 198 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 142 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 120 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 178 | 121 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–11 | 9 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–172 | 80 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 82–144 | 12 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 98–131 | 16 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 116–148 | 31 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 143–159 | 15 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 180–225 | 46 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `8` (QB)
- ❌ Missing segment for action `Action_ThrowPass` on target `8` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BootAway' for track '8' has invalid range: start=98, end=91. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '8' has invalid range: start=156, end=91. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [58–72], lower_priority='Action_RunBlock' annotated_start=68, effective_Action_RunBlock_start=73.
- ⚠️ Action 'Action_RunBlock' range [68-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-172] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [175-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [82-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-154] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-198] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-172] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-225] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '20' has 1 frames without a visible bounding box.
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