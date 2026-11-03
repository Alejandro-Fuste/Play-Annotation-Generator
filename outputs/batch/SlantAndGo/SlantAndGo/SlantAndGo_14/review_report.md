# Play-Annotation-Generator Annotation Review — SlantAndGo_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_14`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellRoute` | Position_Unknown | Team_Unknown | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 3 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `15` | `15` | 1 | START | 4 | 14 |
| ✅ EXACT | `Action_PassBlock` | LT | `13` | `13` | 4 | START | 4 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 4 | START | 4 | 28 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 14 | END | 1 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellRoute` | Position_Unknown | `17` | `17` | 27 | START | 31 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | Position_Unknown | `17` | `17` | 64 | START | 64 | 262 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 75 | START | 75 | 81 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_None` | 15 | 74 | 60 | inferred_complete_timeline |
| `Action_ThrowPass` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 237 | 156 | inferred_complete_timeline |
| `Action_None` | 239 | 251 | 13 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 118 | 86 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 61 | 61 | inferred_complete_timeline |
| `Action_None` | 150 | 299 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 299 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 28 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 122 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 79 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 116 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 132 | 132 | inferred_complete_timeline |
| `Action_None` | 134 | 299 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 100 | 100 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 95 | 95 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 123 | 147 | 25 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 29 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–95 | 95 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 4–299 | 255 | 8 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 27–119 | 90 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 31–299 | 249 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 68–299 | 232 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 81–133 | 51 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 98–299 | 200 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 128–299 | 172 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 132–299 | 168 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 136–299 | 164 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 139–299 | 161 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 157–299 | 143 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–167 | 8 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 201–244 | 20 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 235–299 | 60 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 238–299 | 59 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 269–295 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `15` (Position_Unknown): Annotated start 1 != Inferred start 4
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SellRoute` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `17` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [1-132] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-79] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-100] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-147] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-262] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellRoute' range [31-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [64-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [268-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [271-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [278-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>