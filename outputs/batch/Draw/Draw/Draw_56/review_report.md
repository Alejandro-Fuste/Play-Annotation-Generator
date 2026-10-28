# Play-Annotation-Generator Annotation Review — Draw_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_56`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 60 | START | 60 | 62 |
| ✅ EXACT | `Action_SnapReceive` | RG | `3` | `2` | 62 | END | 60 | 62 |
| ✅ EXACT | `Action_PassBlock` | LT | `1` | `0` | 69 | START | 69 | 158 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `11` | 69 | START | 69 | 158 |
| ✅ EXACT | `Action_PassBlock` | C | `14` | `13` | 69 | START | 69 | 153 |
| ✅ EXACT | `Action_PassBlock` | RG | `3` | `2` | 69 | START | 69 | 158 |
| ✅ EXACT | `Action_PassBlock` | LG | `7` | `6` | 69 | START | 69 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 88 | START | 88 | 109 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 125 | START | 125 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 88 | 109 | 22 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 239 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 200 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 158 | 90 | inferred_complete_timeline |
| `Action_None` | 159 | 199 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 158 | 90 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 153 | 85 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 215 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 158 | 90 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 158 | 90 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 191 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 89 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 72 | 85 | 14 | inferred_complete_timeline |
| `Action_None` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 153 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 11 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_None` | 60 | 73 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–239 | 235 | 5 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–133 | 134 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 15–22 | 8 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 85–239 | 155 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 95–239 | 128 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 110–239 | 128 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 151–239 | 89 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 155–217 | 60 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 164–239 | 76 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 199–239 | 41 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 202–218 | 17 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 224–236 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 112: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [159-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-200] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [88-109] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-133] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-89] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>