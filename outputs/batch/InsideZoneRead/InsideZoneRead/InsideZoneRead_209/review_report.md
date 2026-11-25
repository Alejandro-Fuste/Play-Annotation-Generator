# Play-Annotation-Generator Annotation Review — InsideZoneRead_209

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_209`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `17` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `16` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 56 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 78 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `15` | `13` | 98 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 101 | START | 101 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `14` | 101 | START | 101 | 139 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `17` | `15` | 101 | START | 140 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 101 | START | 101 | 151 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `17` | 118 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `19` | `17` | 131 | START | 164 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `16` | `14` | 140 | START | 140 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 174 | 77 | inferred_complete_timeline |
| `Action_None` | 178 | 248 | 71 | inferred_complete_timeline |
| `Action_None` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 98 | 169 | 72 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 186 | 204 | 19 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 151 | 51 | inferred_complete_timeline |
| `Action_None` | 152 | 215 | 64 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 56–161
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 100 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 139 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 161 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 140–299
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_None` | 152 | 173 | 22 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 151 | 51 | inferred_complete_timeline |
| `Action_None` | 152 | 164 | 13 | inferred_complete_timeline |
| `Action_None` | 169 | 205 | 37 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 252 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 158 | 61 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 153 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 182 | 59 | inferred_complete_timeline |
| `Action_None` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_None` | 209 | 292 | 84 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–299 | 282 | 4 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–30 | 31 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–269 | 262 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–35 | 36 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 45–62 | 18 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 164–228 | 65 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 177–282 | 73 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 197–262 | 65 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 203–299 | 96 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 233–299 | 66 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 233–299 | 60 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 254–299 | 36 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 279–296 | 18 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 280–299 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | 161 | 161 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (Position_Unknown)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (RG): Annotated start 101 != Inferred start 140
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `19` (Position_Unknown): Annotated start 131 != Inferred start 164
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 418: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '13' has invalid range: start=98, end=62. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=164, end=118. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '17' has invalid range: start=164, end=139. Clamping end to start.
- ⚠️ Action 'Action_None' range [152-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-197] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-169] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-204] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-292] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-248] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-62] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-249] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_209'; source metadata written as null.

</details>