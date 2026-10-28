# Play-Annotation-Generator Annotation Review — Draw_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_32`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 70 | START | 70 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `1` | `0` | 73 | START | 73 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `10` | 73 | START | 73 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `2` | 73 | START | 73 | 103 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `5` | `4` | 73 | START | 86 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `7` | 73 | START | 73 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 85 | END | 70 | 85 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 91 | START | 91 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 115 | START | 115 | 133 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–148
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 91 | 114 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 148 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 103 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 151 | 36 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 151 | 66 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 115 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 126 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 103 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 151 | 42 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 175 | 106 | inferred_complete_timeline |
| `Action_None` | 178 | 299 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 107 | 38 | inferred_complete_timeline |
| `Action_None` | 118 | 154 | 37 | inferred_complete_timeline |
| `Action_None` | 156 | 299 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 119 | 50 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 154 | 85 | inferred_complete_timeline |
| `Action_None` | 157 | 238 | 82 | inferred_complete_timeline |
| `Action_None` | 240 | 278 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 178 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `15` | Position_Unknown | Team_Unknown | 130–299 | 165 | 3 | Undefined position; Undefined team |
| `12` | `16` | Position_Unknown | Team_Unknown | 137–299 | 162 | 2 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 155–299 | 142 | 3 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 161–299 | 139 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 164–299 | 136 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 199–291 | 90 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 232–256 | 18 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 245–299 | 55 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 251–253 | 3 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 255–267 | 12 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `5` (C): Annotated start 73 != Inferred start 86
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [70–85], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=86.
- ⚠️ Action 'Action_PassBlock' range [73-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-154] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-178] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>