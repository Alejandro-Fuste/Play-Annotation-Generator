# Play-Annotation-Generator Annotation Review — StopAndGo_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_39`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 5 | START | 5 | 9 |
| ✅ EXACT | `Action_PassBlock` | LG | `12` | `12` | 8 | START | 8 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 8 | START | 8 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 8 | START | 8 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 8 | START | 10 | 126 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 9 | END | 5 | 9 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 19 | START | 19 | 59 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 60 | START | 60 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `0` | `0` | 77 | START | 77 | 195 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 99 | START | 99 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_None` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_ThrowPass` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_None` | 110 | 197 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 208 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 217 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 209 | 205 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 219 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_VerticalStem` | 19 | 59 | 41 | inferred_complete_timeline |
| `Action_SellStop` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 77 | 195 | 119 | inferred_complete_timeline |
| `Action_RunGoRoute` | 199 | 205 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 147 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 173 | 166 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 189 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 203 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 126 | 117 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 147 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 212 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 168 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 189 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 201 | 204 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 54 | 50 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_None` | 93 | 149 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 211 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 39 | 35 | inferred_complete_timeline |
| `Action_None` | 44 | 224 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_None` | 48 | 81 | 34 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 266 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_None` | 50 | 269 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 237 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 269 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 269 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 269 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 229 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–209 | 210 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 90–93 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 137–218 | 82 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 146–259 | 95 | 7 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 155–184 | 29 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 250–258 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [5–9], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=10.
- ⚠️ Action 'Action_RunGoRoute' range [77-195] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [199-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-224] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-237] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-180] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [195-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [201-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-259] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>