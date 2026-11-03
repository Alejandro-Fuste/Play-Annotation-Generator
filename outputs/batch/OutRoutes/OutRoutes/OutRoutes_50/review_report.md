# Play-Annotation-Generator Annotation Review — OutRoutes_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_50`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 76
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_RunOutRoute` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | DE1 | defense | `16` | `16` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_PassBlock` | RT | `10` | `10` | 15 | START | 15 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 15 | START | 15 | 65 |
| ✅ EXACT | `Action_PassBlock` | LG | `7` | `7` | 15 | START | 15 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `8` | `8` | 15 | START | 15 | 24 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `9` | 15 | START | 15 | 84 |
| ❌ MISSING SEGMENT | `Action_RunOutRoute` | Position_Unknown | `23` | `22` | 20 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `16` | `16` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | DE1 | `16` | `16` | 43 | START | 43 | 47 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `23` | `22` | 71 | START | 77 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `22` | 80 | START | 80 | 85 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 84 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 89 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 65 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 100 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 24 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 31 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 94 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 42 | 22 | inferred_complete_timeline |
| `Action_ThrowPass` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 90 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 59 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 88 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 95 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–97 | 98 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 20–94 | 75 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 32–75 | 41 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 50–58 | 7 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 52–77 | 24 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 77–210 | 111 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 87–193 | 107 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–94 | 8 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 91–204 | 114 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 92–96 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 102–210 | 73 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 139–210 | 72 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 163–210 | 33 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 168–210 | 42 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 169–210 | 41 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 188–194 | 7 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `39` | `48` | 207 | 207 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_RunOutRoute` on target `23` (Position_Unknown)
- ⚠️ `Action_SecureCatch` for actor_track_id `23` (Position_Unknown): Annotated start 71 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_RunOutRoute' for track '22' has invalid range: start=77, end=70. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-71] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-24] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [43-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-176] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-204] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-190] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>