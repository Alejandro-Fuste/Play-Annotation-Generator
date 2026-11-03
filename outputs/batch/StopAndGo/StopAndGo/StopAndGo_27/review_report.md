# Play-Annotation-Generator Annotation Review — StopAndGo_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_27`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `3` | `3` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_PumpFake` | QB1 | offense | `3` | `3` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 23 | START | 23 | 36 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `13` | `13` | 29 | START | 38 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `14` | `14` | 29 | START | 29 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 29 | START | 29 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 29 | START | 29 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 29 | START | 29 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `3` | `3` | 37 | END | 23 | 37 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `1` | `1` | 41 | START | 41 | 74 |
| ✅ EXACT | `Action_SellStop` | WR3 | `1` | `1` | 75 | START | 75 | 95 |
| ✅ EXACT | `Action_PumpFake` | QB1 | `3` | `3` | 86 | START | 86 | 98 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `1` | `1` | 96 | START | 96 | 186 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `3` | `3` | 105 | START | 105 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_None` | 38 | 85 | 48 | inferred_complete_timeline |
| `Action_PumpFake` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 118 | 14 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 174 | 152 | inferred_complete_timeline |
| `Action_None` | 181 | 269 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_VerticalStem` | 41 | 74 | 34 | inferred_complete_timeline |
| `Action_SellStop` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 96 | 186 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 123 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 269 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 136 | 108 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 219 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 36 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 85 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 66 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 92 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 269 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 60 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 74 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 103 | 186 | 84 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 204 | 182 | inferred_complete_timeline |
| `Action_None` | 206 | 238 | 33 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 43 | 21 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 190 | 168 | inferred_complete_timeline |
| `Action_None` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 198 | 176 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 218 | 14 | inferred_complete_timeline |
| `Action_None` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 100 | 78 | inferred_complete_timeline |
| `Action_None` | 107 | 181 | 75 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 201 | 16 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 228 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 222 | 200 | inferred_complete_timeline |
| `Action_None` | 225 | 269 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 127 | 105 | inferred_complete_timeline |
| `Action_None` | 130 | 222 | 93 | inferred_complete_timeline |
| `Action_None` | 227 | 235 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 81–269 | 189 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 83–85 | 3 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 128–269 | 134 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 135–269 | 135 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 152–269 | 114 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 164–269 | 68 | 9 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 189–269 | 41 | 6 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 198–247 | 50 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 247–266 | 12 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `13` (C): Annotated start 29 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [23–37], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=38.
- ⚠️ Action 'Action_None' range [23-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [96-186] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-181] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-242] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-102] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [23-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-238] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-163] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-224] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-241] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-247] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>