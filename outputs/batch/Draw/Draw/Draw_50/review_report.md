# Play-Annotation-Generator Annotation Review — Draw_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_50`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 51 | START | 51 | 65 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `9` | 54 | START | 66 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `11` | 54 | START | 54 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 54 | START | 54 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `6` | `5` | 54 | START | 54 | 63 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 65 | END | 51 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 71 | START | 71 | 95 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 107 | START | 107 | 111 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–111
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 71 | 95 | 25 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 111 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 95 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 74 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 146 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 150 | 85 | inferred_complete_timeline |
| `Action_None` | 151 | 197 | 47 | inferred_complete_timeline |
| `Action_None` | 203 | 224 | 22 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 63 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 150 | 48 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 117 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 150 | 31 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

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
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 201 | 151 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 239 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 155 | 105 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 114 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 93 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 74 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–148 | 139 | 4 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 124–238 | 111 | 3 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 155–239 | 84 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 156–239 | 84 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 163–239 | 77 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 167–204 | 34 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 188–239 | 45 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 195–204 | 10 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 198–239 | 42 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 209–239 | 31 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 219–239 | 20 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 54 != Inferred start 66
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [51–65], lower_priority='Action_PassBlock' annotated_start=54, effective_Action_PassBlock_start=66.
- ⚠️ Action 'Action_None' range [51-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-224] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [71-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '25' has 2 frames without a visible bounding box.
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

</details>