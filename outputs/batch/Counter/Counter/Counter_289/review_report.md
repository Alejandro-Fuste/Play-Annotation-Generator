# Play-Annotation-Generator Annotation Review — Counter_289

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_289`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR4 | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 136 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 137 | START | 137 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 140 | START | 150 | 169 |
| ✅ EXACT | `Action_DownBlock` | LT | `21` | `20` | 140 | START | 140 | 168 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `17` | 140 | START | 140 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR4 | `1` | `0` | 140 | START | 140 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 149 | END | 137 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `14` | `13` | 163 | START | 163 | 169 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `16` | 182 | START | 182 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_SnapReceive` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_None` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 140 | 173 | 34 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 194 | 230 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 234 | 239 | 6 | inferred_complete_timeline |
| `Action_None` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 168 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 168 | 32 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_BallSnap` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 169 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 222 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 169 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 166 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 168 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 168 | 32 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 162 | 26 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 219 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 208 | 72 | inferred_complete_timeline |
| `Action_None` | 211 | 223 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 201 | 65 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 216 | 222 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 294 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 226 | 90 | inferred_complete_timeline |
| `Action_None` | 230 | 249 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–167 | 168 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 179–222 | 36 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 191–281 | 82 | 6 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 195–222 | 18 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 235–299 | 61 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 239–294 | 41 | 5 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 269–298 | 29 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 291–299 | 8 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 292–299 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (5 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 580: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [137–149], lower_priority='Action_DownBlock' annotated_start=140, effective_Action_DownBlock_start=150.
- ⚠️ Action 'Action_PullLeadBlock' range [140-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [179-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [186-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [194-230] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-294] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [163-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [172-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [172-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [200-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-222] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-196] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-222] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-294] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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