# Play-Annotation-Generator Annotation Review — Draw_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_97`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 51
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `4` | `3` | 40 | START | 40 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `0` | 43 | START | 43 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `2` | `1` | 43 | START | 43 | 86 |
| ✅ EXACT | `Action_PassBlock` | LG | `3` | `2` | 43 | START | 43 | 136 |
| ✅ EXACT | `Action_PassBlock` | RG | `5` | `4` | 43 | START | 43 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 50 | END | 40 | 50 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 60 | START | 60 | 98 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `6` | 99 | START | 99 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 50 | 11 | inferred_complete_timeline |
| `Action_None` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 60 | 98 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 238 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 79 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 136 | 94 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 136 | 94 | inferred_complete_timeline |
| `Action_None` | 137 | 179 | 43 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 136 | 94 | inferred_complete_timeline |
| `Action_None` | 137 | 190 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 86 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 136 | 43 | inferred_complete_timeline |
| `Action_None` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 50 | 11 | inferred_complete_timeline |
| `Action_None` | 51 | 181 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 139 | 100 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 46 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 106 | 67 | inferred_complete_timeline |
| `Action_None` | 111 | 155 | 45 | inferred_complete_timeline |
| `Action_None` | 165 | 185 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 82 | 43 | inferred_complete_timeline |
| `Action_None` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 93 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 239 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 33–70 | 32 | 6 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 55–239 | 173 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 79–104 | 26 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 106–108 | 3 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 145–239 | 94 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 148–239 | 92 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 181–193 | 9 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 30 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [137-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-86] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-181] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-238] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-139] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-93] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 40, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [40-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-196] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '20' has 1 frames without a visible bounding box.
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

</details>