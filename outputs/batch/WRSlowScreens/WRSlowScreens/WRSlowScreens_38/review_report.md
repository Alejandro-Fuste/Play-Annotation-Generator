# Play-Annotation-Generator Annotation Review — WRSlowScreens_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_38`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `25` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 27 | START | 27 | 44 |
| ✅ EXACT | `Action_PassBlock` | RG | `10` | `10` | 30 | START | 30 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 30 | START | 45 | 182 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `2` | 30 | START | 30 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `3` | 30 | START | 30 | 96 |
| ✅ EXACT | `Action_PassBlock` | LG | `5` | `5` | 30 | START | 30 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 44 | END | 27 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | RG | `10` | `10` | 62 | START | 62 | 93 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `6` | `6` | 105 | START | 105 | 114 |
| ✅ EXACT | `Action_RunAfterCatch` | Position_Unknown | `25` | `20` | 134 | START | 134 | 172 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 45 | 104 | 60 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 95 | 69 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 124 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 96 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 101 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 127 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 182 | 138 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 62 | 93 | 32 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 124 | 157 | 34 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 117 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |
| `Action_None` | 129 | 137 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 60 | 34 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 105 | 25 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_None` | 35 | 122 | 88 | inferred_complete_timeline |
| `Action_None` | 125 | 133 | 9 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 99 | 73 | inferred_complete_timeline |
| `Action_None` | 102 | 120 | 19 | inferred_complete_timeline |
| `Action_None` | 124 | 163 | 40 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 53 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 98 | 72 | inferred_complete_timeline |
| `Action_None` | 100 | 117 | 18 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 35–121 | 87 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 64–65 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 74–210 | 137 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 80–122 | 43 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 104–123 | 19 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 124–172 | 49 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 130–166 | 34 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 136–210 | 71 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 168–210 | 36 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 177–181 | 5 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 181–200 | 20 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 196–210 | 14 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReleaseToScreen` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [27–44], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=45.
- ⚠️ Action 'Action_None' range [27-120] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-124] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [62-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [124-157] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [161-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [134-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>