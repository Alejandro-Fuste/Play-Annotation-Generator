# Play-Annotation-Generator Annotation Review — Counter_264

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_264`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 78
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | FB | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `16` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 44 | START | 44 | 59 |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `13` | 47 | START | 47 | 107 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `5` | `4` | 47 | START | 60 | 128 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `8` | 47 | START | 47 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `9` | 47 | START | 47 | 58 |
| ✅ EXACT | `Action_PullLeadBlock` | FB | `16` | `15` | 47 | START | 47 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 59 | END | 44 | 59 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `4` | `3` | 89 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_None` | 60 | 75 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 73 | 30 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 47 | 76 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 96 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 107 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 128 | 69 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 158 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 83 | 118 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |
| `Action_None` | 106 | 153 | 48 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 150 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 102 | 59 | inferred_complete_timeline |
| `Action_None` | 106 | 150 | 45 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 119 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 160 | 117 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 117 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 62–210 | 119 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 77–112 | 31 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 92–123 | 29 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 97–139 | 43 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 102–176 | 73 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 103–210 | 85 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 106–210 | 105 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 109–132 | 24 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 112–210 | 99 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 113–210 | 94 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 116–144 | 29 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 129–210 | 79 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 150–210 | 59 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 191–209 | 19 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `29` | `36` | 155 | 155 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `5` (C): Annotated start 47 != Inferred start 60
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=89, end=75. Clamping end to start.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [44–59], lower_priority='Action_DownBlock' annotated_start=47, effective_Action_DownBlock_start=60.
- ⚠️ Action 'Action_None' range [44-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [47-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [83-118] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-102] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-73] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [47-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-176] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>