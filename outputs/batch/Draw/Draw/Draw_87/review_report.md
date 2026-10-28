# Play-Annotation-Generator Annotation Review — Draw_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_87`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 26 | START | 26 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `13` | 29 | START | 40 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `1` | 29 | START | 29 | 64 |
| ✅ EXACT | `Action_PassBlock` | RT | `3` | `2` | 29 | START | 29 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `5` | `4` | 29 | START | 29 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 39 | END | 26 | 39 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `12` | `11` | 41 | START | 41 | 78 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 79 | START | 79 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 138 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 41 | 78 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 155 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 38 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 58 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 65 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 138 | 42 | inferred_complete_timeline |
| `Action_None` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 64 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 138 | 110 | inferred_complete_timeline |
| `Action_None` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 34 | 9 | inferred_complete_timeline |
| `Action_None` | 72 | 159 | 88 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 102 | 77 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 169 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 188 | 163 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 66 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–239 | 221 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 47–239 | 184 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 79–239 | 115 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 105–239 | 119 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 161–239 | 79 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 167–239 | 73 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 170–239 | 68 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 177–189 | 13 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 178–197 | 20 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 216–239 | 24 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 174: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [26–39], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=40.
- ⚠️ Action 'Action_None' range [26-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-65] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>