# Play-Annotation-Generator Annotation Review — InsideZoneRead_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_44`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 2
- **Action Segments:** 68
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `14` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `18` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 47 | START | 47 | 63 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 49 | START | 64 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 49 | START | 49 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 49 | START | 49 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 49 | START | 49 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 49 | START | 49 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | `16` | `14` | 63 | END | 47 | 52 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `16` | `14` | 68 | START | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 78 | START | 78 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `18` | 89 | START | 116 | 137 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `12` | `11` | 89 | START | 89 | 160 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 160 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_Handoff` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 113 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 245 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 140 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 160 | 112 | inferred_complete_timeline |
| `Action_None` | 161 | 209 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 89 | 160 | 72 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 160 | 112 | inferred_complete_timeline |
| `Action_None` | 161 | 196 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 160 | 112 | inferred_complete_timeline |
| `Action_None` | 161 | 299 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 201 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 252 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 116 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 129 | 83 | inferred_complete_timeline |
| `Action_None` | 133 | 206 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 299 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 254 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 9–62 | 35 | 4 | Undefined position; Undefined team |
| `15` | `22` | Position_Unknown | Team_Unknown | 76–81 | 6 | 1 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 113–232 | 120 | 1 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 115–119 | 5 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 116–215 | 95 | 3 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 137–299 | 163 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 139–299 | 161 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 139–151 | 13 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 160–299 | 140 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 180–299 | 120 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 181–186 | 6 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 185–250 | 62 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 186–251 | 54 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 192–196 | 5 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 194–299 | 106 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 195–203 | 5 | 2 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 214–229 | 16 | 1 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 266–299 | 32 | 3 | Undefined position; Undefined team |
| `36` | `62` | Position_Unknown | Team_Unknown | 285–299 | 14 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | 8 | 41 | 25 | 73.5% | 15–18, 24–27, 36 |
| `33` | `56` | 240 | 240 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 49 != Inferred start 64
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 112 frames exceeds threshold 90 frames [start=49, end=160].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 112 frames exceeds threshold 90 frames [start=49, end=160].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 112 frames exceeds threshold 90 frames [start=49, end=160].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 92 frames exceeds threshold 90 frames [start=49, end=140].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [47–63], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=64.
- ⚠️ Segment 'Action_ReadDefender' for track '14' has invalid range: start=68, end=62. Clamping end to start.
- ⚠️ Action 'Action_None' range [47-252] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-245] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-206] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [47-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [61-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-148] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-215] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-245] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-290] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '36' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>