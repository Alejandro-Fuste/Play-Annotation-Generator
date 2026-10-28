# Play-Annotation-Generator Annotation Review — Draw_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 63
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 3 | START | 3 | 19 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `11` | 6 | START | 20 | 90 |
| ✅ EXACT | `Action_PassBlock` | RT | `3` | `2` | 6 | START | 6 | 90 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 6 | START | 6 | 90 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `8` | 6 | START | 6 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 19 | END | 3 | 19 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `8` | `7` | 22 | START | 22 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 50 | START | 50 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 90 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 22 | 49 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 230 | 181 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 48 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 90 | 85 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 90 | 71 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 90 | 85 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 90 | 85 | inferred_complete_timeline |
| `Action_None` | 91 | 113 | 23 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

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
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 43 | 41 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 106 | 104 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 239 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 45 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 112 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 109 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 3–50 | 44 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 51–239 | 171 | 3 | Undefined position; Undefined team |
| `14` | `19` | Position_Unknown | Team_Unknown | 81–239 | 159 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 129–239 | 72 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 135–161 | 27 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 142–161 | 20 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 162–239 | 75 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 162–191 | 30 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–239 | 77 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 181–239 | 59 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 6 != Inferred start 20
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 26 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 166: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [3-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-230] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-8] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-50] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-191] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>