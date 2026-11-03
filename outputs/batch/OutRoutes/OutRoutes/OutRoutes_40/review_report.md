# Play-Annotation-Generator Annotation Review — OutRoutes_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_40`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 38
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 21
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | SAF1 | defense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `40` | `25` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `40` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 31 | START | 31 | 49 |
| ✅ EXACT | `Action_PassBlock` | C | `2` | `2` | 31 | START | 31 | 113 |
| ✅ EXACT | `Action_PassBlock` | LG | `5` | `5` | 31 | START | 31 | 180 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 31 | START | 31 | 36 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `9` | 31 | START | 31 | 134 |
| ✅ EXACT | `Action_RunOutRoute` | SAF1 | `7` | `7` | 37 | START | 37 | 113 |
| ✅ EXACT | `Action_SnapReceive` | RT | `8` | `8` | 37 | END | 37 | 37 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RT | `8` | `8` | 121 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `40` | `25` | 142 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `40` | `25` | 150 | START | 156 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 134 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 180 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 113 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 88 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 111 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 180 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunOutRoute` | 37 | 113 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 59–115 | 57 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 86–101 | 16 | 1 | Undefined position; Undefined team |
| `18` | `29` | Position_Unknown | Team_Unknown | 93–180 | 88 | 1 | Undefined position; Undefined team |
| `19` | `30` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `20` | `32` | Position_Unknown | Team_Unknown | 110–180 | 71 | 1 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 115–164 | 50 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 120–180 | 61 | 1 | Undefined position; Undefined team |
| `23` | `38` | Position_Unknown | Team_Unknown | 147–180 | 34 | 1 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 156–180 | 25 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 156–180 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `8` (RT)
- ❌ Missing segment for action `Action_SecureCatch` on target `25` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `40` (Position_Unknown): Annotated start 150 != Inferred start 156

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '8' has invalid range: start=121, end=88. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '25' has invalid range: start=156, end=149. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-113] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-111] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [37-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-88] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-180] for track '25' has 1 frames without a visible bounding box.
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

</details>