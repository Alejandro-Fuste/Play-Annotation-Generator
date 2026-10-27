# Play-Annotation-Generator Annotation Review — Counter_348

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_348`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 49
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
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 45 | START | 45 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `3` | 48 | START | 48 | 73 |
| ✅ EXACT | `Action_DownBlock` | LG | `7` | `6` | 48 | START | 48 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `12` | `11` | 48 | START | 59 | 93 |
| ✅ EXACT | `Action_PullLeadBlock` | RG | `9` | `8` | 48 | START | 48 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 58 | END | 45 | 58 |
| ✅ EXACT | `Action_Handoff` | QB | `1` | `0` | 68 | START | 68 | 83 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `1` | 84 | START | 84 | 162 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_None` | 59 | 67 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 173 | 90 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 162 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 114 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 127 | 80 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 59 | 93 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 95 | 127 | 33 | inferred_complete_timeline |
| `Action_None` | 128 | 171 | 44 | inferred_complete_timeline |
| `Action_None` | 177 | 216 | 40 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 48 | 127 | 80 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 127 | 40 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 97 | 53 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 110 | 66 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 147 | 103 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 195 | 151 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 48–239 | 192 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 94–239 | 146 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 130–195 | 59 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 130–239 | 108 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 130–138 | 7 | 3 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 165–239 | 75 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 213–239 | 27 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [45–58], lower_priority='Action_PullBlock' annotated_start=48, effective_Action_PullBlock_start=59.
- ⚠️ Action 'Action_Handoff' range [68-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-173] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-73] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-195] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-147] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [59-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-239] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '18' has 1 frames without a visible bounding box.
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

</details>