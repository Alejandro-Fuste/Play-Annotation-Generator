# Play-Annotation-Generator Annotation Review — Counter_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_202`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `8` | `7` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 85 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `8` | `7` | 86 | START | 86 | 87 |
| ✅ EXACT | `Action_DownBlock` | LT | `10` | `9` | 88 | START | 88 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `5` | `4` | 88 | START | 88 | 116 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `8` | `7` | 88 | START | 88 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `6` | 88 | START | 88 | 125 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `1` | `0` | 88 | START | 88 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 99 | END | 86 | 99 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 130 | START | 130 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 152 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 100 | 129 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 269 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 159 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 116 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 152 | 35 | inferred_complete_timeline |
| `Action_None` | 153 | 175 | 23 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 221 | 136 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PullBlock` | 88 | 125 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 152 | 26 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 161 | 76 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 139 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 269 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 269 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 269 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 225 | 140 | inferred_complete_timeline |
| `Action_None` | 227 | 269 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 145 | 60 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–268 | 269 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 53–121 | 69 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 72–114 | 43 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 138–269 | 132 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 141–197 | 57 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 177–269 | 93 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 181–269 | 88 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 191–269 | 79 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 204–212 | 9 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 211–269 | 58 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 219–269 | 51 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 24 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 405: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [86-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-139] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [88-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-159] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>