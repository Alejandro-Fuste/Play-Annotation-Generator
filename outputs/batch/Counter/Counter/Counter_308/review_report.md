# Play-Annotation-Generator Annotation Review — Counter_308

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_308`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT3 | defense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 57 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | `12` | `11` | 58 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `12` | `11` | 61 | START | 62 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `2` | 61 | START | 61 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `2` | 61 | START | 61 | 86 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `3` | 61 | START | 61 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT3 | `17` | `16` | 61 | START | 65 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 73 | END | 58 | 73 |
| ✅ EXACT | `Action_BallCarry` | QB | `8` | `7` | 95 | START | 95 | 209 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 94 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 209 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 116 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 132 | 45 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_None` | 83 | 128 | 46 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PullBlock` | 61 | 74 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 152 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 108 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 120 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 65–152
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PullLeadBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 106 | 19 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_None` | 133 | 152 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 113 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 176 | 119 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 9–210 | 186 | 8 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 45–210 | 164 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 49–132 | 80 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 85–210 | 117 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 130–133 | 4 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 140–210 | 71 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 147–210 | 64 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 171–210 | 31 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `12` (DT1)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Deduplicated duplicate event 'Action_DownBlock' at frame 61 for track '2'.
- ⚠️ Action 'Action_None' range [58-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [61-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [61-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-120] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [65-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [68-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [88-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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