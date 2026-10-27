# Play-Annotation-Generator Annotation Review — Counter_258

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_258`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 89 | START | 89 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `5` | `4` | 92 | START | 94 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `6` | `5` | 92 | START | 92 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `9` | `8` | 92 | START | 92 | 137 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `6` | 92 | START | 92 | 154 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `10` | `9` | 92 | START | 92 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 93 | END | 89 | 93 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 118 | START | 118 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 133 | START | 133 | 291 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 117 | 24 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_None` | 133 | 299 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 291 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 92 | 158 | 67 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 219 | 131 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PullBlock` | 92 | 154 | 63 | inferred_complete_timeline |
| `Action_None` | 161 | 203 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 158 | 65 | inferred_complete_timeline |
| `Action_None` | 159 | 288 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 141 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 231 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 137 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 157 | 19 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 274 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 194 | 106 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 158 | 70 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 154 | 66 | inferred_complete_timeline |
| `Action_None` | 210 | 238 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 266 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 71–221 | 142 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 104–139 | 36 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 114–299 | 186 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 118–131 | 14 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 142–299 | 158 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 144–299 | 156 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 156–294 | 139 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 157–240 | 84 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 181–186 | 6 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 188–215 | 28 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 199–272 | 69 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 203–299 | 94 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 218–226 | 9 | 1 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [89–93], lower_priority='Action_DownBlock' annotated_start=92, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_None' range [89-194] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [92-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-157] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-274] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-154] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-160] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-294] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-240] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-215] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>