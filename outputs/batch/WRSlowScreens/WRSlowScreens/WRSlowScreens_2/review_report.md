# Play-Annotation-Generator Annotation Review — WRSlowScreens_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ReleaseToScreen` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowScreenPass` | LB2 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `2` | 8 | START | 8 | 25 |
| ✅ EXACT | `Action_PassBlock` | LT | `1` | `1` | 11 | START | 11 | 239 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `2` | `2` | 11 | START | 26 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `5` | `5` | 11 | START | 11 | 138 |
| ✅ EXACT | `Action_PassBlock` | LG | `7` | `7` | 11 | START | 11 | 35 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 11 | START | 11 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 25 | END | 8 | 25 |
| ✅ EXACT | `Action_ReleaseToScreen` | LG | `7` | `7` | 36 | START | 36 | 80 |
| ✅ EXACT | `Action_ThrowScreenPass` | LB2 | `4` | `4` | 67 | START | 67 | 77 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_None` | 26 | 112 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 79 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 87 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 35 | 25 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 36 | 80 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 156 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 138 | 128 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 91 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 134 | 127 | inferred_complete_timeline |
| `Action_None` | 139 | 163 | 25 | inferred_complete_timeline |
| `Action_None` | 165 | 182 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 92 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 30 | 23 | inferred_complete_timeline |
| `Action_None` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_None` | 40 | 127 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 43 | 36 | inferred_complete_timeline |
| `Action_None` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_None` | 54 | 239 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 95 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 67 | 77 | 11 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 70 | 86 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–54 | 21 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 81–239 | 157 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 84–91 | 8 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 91–226 | 131 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 93–239 | 130 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 96–239 | 139 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 96–239 | 144 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 102–239 | 133 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 141–239 | 99 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 151–177 | 9 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 155–239 | 78 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 166–230 | 56 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 166–211 | 46 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 175–239 | 64 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 209–239 | 31 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 219–239 | 19 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `2` (C): Annotated start 11 != Inferred start 26
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [8–25], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=26.
- ⚠️ Action 'Action_None' range [8-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [36-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-112] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-7] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-215] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-231] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>