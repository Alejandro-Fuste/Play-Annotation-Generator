# Play-Annotation-Generator Annotation Review — StopAndGo_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_31`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 3 | START | 3 | 19 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 6 | START | 6 | 192 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 6 | START | 20 | 192 |
| ✅ EXACT | `Action_PassBlock` | RT | `17` | `17` | 6 | START | 6 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 6 | START | 6 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 6 | START | 6 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 19 | END | 3 | 19 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `3` | `3` | 19 | START | 19 | 72 |
| ✅ EXACT | `Action_SellStop` | WR3 | `3` | `3` | 73 | START | 73 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `3` | `3` | 91 | START | 91 | 109 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 92 | START | 92 | 104 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_ThrowPass` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_None` | 105 | 173 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 235 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 213 | 211 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 223 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_VerticalStem` | 19 | 72 | 54 | inferred_complete_timeline |
| `Action_SellStop` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_RunGoRoute` | 91 | 109 | 19 | inferred_complete_timeline |
| `Action_RunGoRoute` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 202 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 192 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 179 | 174 | inferred_complete_timeline |
| `Action_PassBlock` | 181 | 185 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 192 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 124 | 119 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 197 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 44 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 163 | 118 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 196 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_None` | 191 | 203 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 199 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 211 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 203 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 217 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 59 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 173 | 171 | inferred_complete_timeline |
| `Action_None` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 261 | 259 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–214 | 202 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 59–113 | 55 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–125 | 17 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 130–269 | 139 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 155–194 | 40 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 161–212 | 48 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 6 != Inferred start 20
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [3-217] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-44] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-196] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [91-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [117-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-199] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [181-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-113] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-269] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>