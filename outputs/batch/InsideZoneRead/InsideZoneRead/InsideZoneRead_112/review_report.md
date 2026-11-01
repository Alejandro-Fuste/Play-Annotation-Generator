# Play-Annotation-Generator Annotation Review — InsideZoneRead_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_112`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 69
- **Validation Warnings:** 79
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 7 | START | 7 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 7 | START | 7 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 7 | START | 7 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 7 | START | 7 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 7 | START | 7 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 7 | START | 7 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 17 | START | 17 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 20 | START | 20 | 74 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `12` | `11` | 20 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 20 | START | 20 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 20 | START | 20 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 34 | START | 34 | 48 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 49 | START | 49 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 67 | START | 67 | 80 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 90 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 7–159
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_None` | 67 | 159 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 7–179
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 66 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 167 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 90 | 71 | inferred_complete_timeline |
| `Action_None` | 91 | 163 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–139
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 74 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 139 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–19
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 19 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 7–135
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 75 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 135 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 7–143
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 94 | 78 | inferred_complete_timeline |
| `Action_None` | 98 | 128 | 31 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–93
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 93 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 127 | 111 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 29–43
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 29 | 43 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–153
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 153 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 136 | 120 | inferred_complete_timeline |
| `Action_None` | 138 | 198 | 61 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 216 | 227 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 7–79 | 73 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 7–137 | 128 | 3 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 62–82 | 21 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 79–239 | 161 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 85–107 | 23 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 86–140 | 51 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 93–107 | 14 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 98–197 | 98 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 148–168 | 21 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 151–239 | 55 | 4 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 154–239 | 78 | 4 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 174–239 | 66 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `17` | 30 | 31 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 226: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=20, end=19. Clamping end to start.
- ⚠️ Action 'Action_None' range [17-94] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-137] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-159] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [17-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-239] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-107] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-225] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-219] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>