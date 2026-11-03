# Play-Annotation-Generator Annotation Review — StopAndGo_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_1`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 20 | START | 20 | 36 |
| ✅ EXACT | `Action_PassBlock` | LT | `13` | `13` | 23 | START | 23 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 23 | START | 23 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 23 | START | 37 | 252 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 23 | START | 23 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 23 | START | 23 | 203 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 36 | END | 20 | 36 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `12` | `12` | 36 | START | 36 | 77 |
| ✅ EXACT | `Action_SellStop` | WR1 | `12` | `12` | 78 | START | 78 | 90 |
| ✅ EXACT | `Action_PumpFake` | QB | `15` | `15` | 84 | START | 84 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `12` | `12` | 91 | START | 91 | 99 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 112 | START | 112 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_None` | 37 | 83 | 47 | inferred_complete_timeline |
| `Action_PumpFake` | 84 | 111 | 28 | inferred_complete_timeline |
| `Action_ThrowPass` | 112 | 126 | 15 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 79 | 60 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_VerticalStem` | 36 | 77 | 42 | inferred_complete_timeline |
| `Action_SellStop` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_RunGoRoute` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_RunGoRoute` | 108 | 117 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 203 | 181 | inferred_complete_timeline |
| `Action_PassBlock` | 205 | 260 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 252 | 216 | inferred_complete_timeline |
| `Action_PassBlock` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 149 | 127 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 269 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 109 | 90 | inferred_complete_timeline |
| `Action_None` | 119 | 160 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 182 | 163 | inferred_complete_timeline |
| `Action_None` | 184 | 243 | 60 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 117 | 98 | inferred_complete_timeline |
| `Action_None` | 130 | 199 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 189 | 170 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 56 | 37 | inferred_complete_timeline |
| `Action_None` | 60 | 198 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 154 | 135 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 222 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 218 | 199 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 234 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `28` | Position_Unknown | Team_Unknown | 121–125 | 5 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 161–214 | 42 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 201–269 | 48 | 5 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 208–269 | 11 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 217–265 | 42 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 219–269 | 51 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 223–232 | 6 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 237–241 | 4 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 249–254 | 6 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [20–36], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [20-269] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-198] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-234] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-199] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [91-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [108-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-154] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-149] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-160] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-252] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [260-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [205-260] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-196] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>