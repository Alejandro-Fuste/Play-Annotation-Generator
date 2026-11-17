# Play-Annotation-Generator Annotation Review — Power_162

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_162`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | TE | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 24 | START | 24 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 24 | START | 24 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 24 | START | 24 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 24 | START | 24 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 24 | START | 24 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 24 | START | 24 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `0` | `0` | 125 | START | 125 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `9` | `9` | 125 | START | 125 | 145 |
| ✅ EXACT | `Action_PullBlock` | TE | `5` | `5` | 125 | START | 125 | 179 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 240 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–187
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 122 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 124 | 1 | inferred_complete_timeline |
| `Action_PullBlock` | 125 | 179 | 55 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–262
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 124 | 101 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 158 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 179 | 12 | inferred_complete_timeline |
| `Action_None` | 180 | 228 | 49 | inferred_complete_timeline |
| `Action_None` | 233 | 262 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–169
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 144 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–161
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 139 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 161 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–202
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 177 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 202 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–228
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 228 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 24–125
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 120 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 24–121
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 121 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 133 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 153 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 180 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–209
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 126 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 180 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 209 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–268
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 140 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 165 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 204 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 263 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 24–231 | 200 | 6 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 112–267 | 144 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 121–269 | 145 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 134–157 | 24 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 138–180 | 40 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 143–269 | 110 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 151–269 | 116 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 166–269 | 83 | 5 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 169–268 | 42 | 6 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 175–179 | 5 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 199–269 | 71 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 206–269 | 57 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 212–269 | 58 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 213–269 | 56 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 251–269 | 17 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 261–269 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 325: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 326: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [125-158] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-166] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [168-179] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-177] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-204] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-228] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-144] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-206] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-143] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-177] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-203] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-215] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-262] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>