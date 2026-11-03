# Play-Annotation-Generator Annotation Review — OutRoutes_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_66`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | SAF | defense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `24` | `21` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `24` | `21` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_PassBlock` | C | `10` | `10` | 30 | START | 30 | 72 |
| ✅ EXACT | `Action_PassBlock` | LG | `12` | `12` | 30 | START | 30 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 30 | START | 30 | 65 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `7` | 30 | START | 30 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 30 | START | 30 | 70 |
| ✅ EXACT | `Action_RunOutRoute` | LG | `12` | `12` | 35 | START | 35 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | SAF | `9` | `9` | 35 | START | 35 | 68 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `24` | `21` | 35 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `24` | `21` | 63 | START | 69 | 72 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | DE2 | `1` | `1` | 98 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DE2 | `1` | `1` | 108 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 65 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 72 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_RunOutRoute` | 35 | 65 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 72 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 65 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 70 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 74 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunOutRoute` | 35 | 68 | 34 | inferred_complete_timeline |
| `Action_RunOutRoute` | 72 | 79 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–61 | 62 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 55–62 | 4 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 59–61 | 3 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 63–68 | 6 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 69–71 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 69–72 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 73–210 | 84 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 73–86 | 14 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 73–87 | 15 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 73–105 | 33 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 78–210 | 132 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 82–181 | 100 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 124–131 | 7 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 126–128 | 3 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 128–210 | 74 | 4 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 134–206 | 73 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 140–144 | 5 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 163–172 | 7 | 2 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 171–210 | 10 | 3 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 182–191 | 9 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 187–210 | 19 | 3 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 202–208 | 4 | 2 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (Position_Unknown)
- ⚠️ `Action_ThrowPass` for actor_track_id `24` (Position_Unknown): Annotated start 63 != Inferred start 69
- ❌ Missing segment for action `Action_SecureCatch` on target `1` (DE2)
- ❌ Missing segment for action `Action_BallCarry` on target `1` (DE2)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 74: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '1' has invalid range: start=98, end=68. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=108, end=68. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '21' has invalid range: start=69, end=35. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [35-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [72-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [35-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [69-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-86] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-87] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-105] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-181] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-177] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-190] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-206] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-144] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-190] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-191] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-193] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-201] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>