# Play-Annotation-Generator Annotation Review — InsideZoneRead_304

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_304`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 23 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `15` | 21 | START | 32 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 24 | START | 24 | 35 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 24 | START | 24 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 34 | END | 21 | 34 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 39 | START | 39 | 42 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `17` | `16` | 41 | START | 41 | 42 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 43 | START | 43 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 61 | START | 61 | 62 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_Keep` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 142 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 209 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 236 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 20 | 7 | inferred_complete_timeline |
| `Action_None` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_None` | 28 | 53 | 26 | inferred_complete_timeline |
| `Action_None` | 57 | 152 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 82 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 96 | 73 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 35 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 96 | 1 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 118 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 29 | 98 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 51 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 47 | 27 | inferred_complete_timeline |
| `Action_None` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_None` | 63 | 83 | 21 | inferred_complete_timeline |
| `Action_None` | 85 | 113 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 45 | 25 | inferred_complete_timeline |
| `Action_None` | 51 | 55 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 78 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 71 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 116 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 35 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–182 | 183 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–239 | 229 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 32–39 | 8 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 32–42 | 11 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 55–239 | 183 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 74–87 | 9 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 79–214 | 128 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 101–151 | 46 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 107–129 | 23 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 110–160 | 51 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 111–113 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 128–136 | 9 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 147–239 | 93 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 155–182 | 28 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 195–214 | 13 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 218–231 | 8 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 21 != Inferred start 32
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 608: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 608: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [21-182] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-35] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-51] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-83] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [43-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-236] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-152] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-50] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [41-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-170] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-197] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>