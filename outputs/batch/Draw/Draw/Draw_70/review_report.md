# Play-Annotation-Generator Annotation Review — Draw_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 19 | START | 19 | 34 |
| ✅ EXACT | `Action_PassBlock` | LT | `1` | `0` | 22 | START | 22 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `10` | `9` | 22 | START | 22 | 115 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `10` | 22 | START | 35 | 115 |
| ✅ EXACT | `Action_PassBlock` | RG | `6` | `5` | 22 | START | 22 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `8` | 22 | START | 22 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 34 | END | 19 | 34 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `5` | `4` | 41 | START | 41 | 65 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 66 | START | 66 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_None` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 41 | 65 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 63 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 115 | 94 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 115 | 94 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 115 | 81 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 115 | 94 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 115 | 94 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 147 | 129 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 67 | 49 | inferred_complete_timeline |
| `Action_None` | 71 | 239 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 234 | 216 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 50 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 84 | 66 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 222 | 133 | inferred_complete_timeline |
| `Action_None` | 225 | 233 | 9 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 6–239 | 226 | 6 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 59–190 | 132 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 135–239 | 102 | 4 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 146–239 | 87 | 3 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 148–239 | 92 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 152–239 | 87 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 178–239 | 21 | 8 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 187–239 | 53 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 194–199 | 5 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 206–218 | 13 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 22 != Inferred start 35
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [19–34], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=35.
- ⚠️ Action 'Action_None' range [19-67] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-63] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-222] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>