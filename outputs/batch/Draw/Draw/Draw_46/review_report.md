# Play-Annotation-Generator Annotation Review — Draw_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_46`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Slide`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 49
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `1` | 38 | START | 38 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `1` | `0` | 41 | START | 41 | 113 |
| ✅ EXACT | `Action_PassBlock` | RT | `10` | `9` | 41 | START | 41 | 113 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `2` | `1` | 41 | START | 58 | 113 |
| ✅ EXACT | `Action_PassBlock` | RG | `6` | `5` | 41 | START | 41 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 57 | END | 38 | 57 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `4` | `3` | 62 | START | 62 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 95 | START | 95 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 62 | 94 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 230 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 113 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 113 | 56 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 113 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 231 | 118 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 113 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 200 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 201 | 164 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 123 | 86 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 101 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 148 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 97 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–184 | 184 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 71–239 | 121 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 134–141 | 8 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 156–239 | 82 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 164–239 | 75 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 184–239 | 56 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 187–239 | 53 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `2` (C): Annotated start 41 != Inferred start 58
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 20 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 92: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [38–57], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=58.
- ⚠️ Action 'Action_None' range [114-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-184] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-123] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-101] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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