# Play-Annotation-Generator Annotation Review — WRSlowScreens_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `13` | `13` |
| ✅ EXACT | `Action_ReleaseToScreen` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowScreenPass` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `25` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 0 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | QB | `14` | `14` | 1 | START | 1 | 4 |
| ✅ EXACT | `Action_PassBlock` | LT | `0` | `0` | 4 | START | 4 | 28 |
| ✅ EXACT | `Action_PassBlock` | LG | `2` | `2` | 4 | START | 4 | 210 |
| ✅ EXACT | `Action_PassBlock` | RG | `3` | `3` | 4 | START | 4 | 88 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `7` | 4 | START | 4 | 80 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `13` | `13` | 8 | END | 1 | 8 |
| ✅ EXACT | `Action_ReleaseToScreen` | LT | `0` | `0` | 29 | START | 29 | 36 |
| ✅ EXACT | `Action_ThrowScreenPass` | Position_Unknown | `15` | `15` | 55 | START | 55 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | `25` | `22` | 87 | START | 87 | 133 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 4 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_None` | 9 | 32 | 24 | inferred_complete_timeline |
| `Action_None` | 35 | 81 | 47 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 83 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 73 | 73 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 28 | 25 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 29 | 36 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 88 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 80 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 8 | 8 | inferred_complete_timeline |
| `Action_None` | 9 | 11 | 3 | inferred_complete_timeline |
| `Action_None` | 20 | 30 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 6 | 6 | inferred_complete_timeline |
| `Action_None` | 18 | 58 | 41 | inferred_complete_timeline |
| `Action_None` | 61 | 210 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 18 | 37 | 20 | inferred_complete_timeline |
| `Action_None` | 39 | 56 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 6 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 20 | 20 | inferred_complete_timeline |
| `Action_None` | 22 | 36 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 14–210 | 197 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 17–22 | 5 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 36–92 | 57 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 39–147 | 105 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 51–58 | 8 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 83–172 | 87 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 86–138 | 50 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 95–210 | 72 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 125–165 | 24 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 155–210 | 40 | 6 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 172–210 | 39 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `25` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ReleaseToScreen' range [29-36] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-20] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-58] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [1-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-147] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-147] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [87-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '26' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>