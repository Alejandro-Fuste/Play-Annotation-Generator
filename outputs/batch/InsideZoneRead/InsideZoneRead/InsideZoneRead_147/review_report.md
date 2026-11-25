# Play-Annotation-Generator Annotation Review — InsideZoneRead_147

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_147`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 3
- **Action Segments:** 60
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 7
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `14` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `16` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 35 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `23` | `17` | 318 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 321 | START | 321 | 329 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `11` | `10` | 321 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `7` | `6` | 321 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `8` | `7` | 321 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `16` | `14` | 334 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `16` | `14` | 338 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `16` | `14` | 363 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 412 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 141 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 320 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 303 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 306 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 127 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 245 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 257 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 244 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 2–116 | 115 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 84–242 | 159 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 92–157 | 61 | 5 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 124–142 | 19 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 138–253 | 99 | 7 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 159–242 | 79 | 4 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 166–329 | 164 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 185–190 | 6 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 197–328 | 130 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 197–328 | 132 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 201–276 | 76 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 206–284 | 79 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 213–232 | 19 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 251–253 | 3 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | 49 | 72 | 24 | 100.0% | None |
| `26` | `40` | 248 | 248 | 1 | 100.0% | None |
| `28` | `43` | 263 | 263 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `23` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RT)
- ❌ Missing segment for action `Action_SnapReceive` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (Position_Unknown)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 4 |
| Other | 6 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=321, end=306. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=321, end=175. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=321, end=253. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=318, end=242. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-303] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-141] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-116] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-157] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-249] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-217] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-190] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-316] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-317] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-276] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 334. Video range is [0, 329].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 338. Video range is [0, 329].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 363. Video range is [0, 329].
- ⚠️ Action event 'Action_None' has invalid start frame 412. Video range is [0, 329].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_147'; source metadata written as null.

</details>