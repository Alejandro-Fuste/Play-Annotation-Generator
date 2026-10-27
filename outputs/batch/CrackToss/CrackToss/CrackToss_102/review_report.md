# Play-Annotation-Generator Annotation Review — CrackToss_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_102`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | SAF2 | defense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `19` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 117 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `17` | `16` | 118 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | SAF2 | `11` | `10` | 121 | START | 121 | 201 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 121 | END | 118 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `19` | `17` | 123 | START | 123 | 156 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 126 | START | 126 | 147 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `5` | `4` | 148 | START | 148 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_SnapReceive` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_Toss` | 126 | 147 | 22 | inferred_complete_timeline |
| `Action_None` | 148 | 178 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 219 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 135 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 249 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 220 | 103 | inferred_complete_timeline |
| `Action_None` | 222 | 231 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_None` | 125 | 249 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 249 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 244 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 249 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 185 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 131 | 14 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 156 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 131 | 14 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 173 | 56 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 242 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 142 | 25 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_None` | 150 | 249 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PullBlock` | 121 | 201 | 81 | inferred_complete_timeline |
| `Action_None` | 202 | 249 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–204 | 204 | 3 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–249 | 249 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 123–165 | 37 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 145–158 | 14 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 153–243 | 68 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 153–249 | 93 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 154–157 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 162–249 | 86 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 164–249 | 84 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 187–249 | 63 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 198–249 | 52 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 209–249 | 38 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 229–249 | 21 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 232–236 | 5 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 232–236 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 202: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 202: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 202: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Action 'Action_None' range [118-200] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-219] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-249] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-185] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-220] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [123-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [163-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-241] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>