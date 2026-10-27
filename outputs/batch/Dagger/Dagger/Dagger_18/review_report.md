# Play-Annotation-Generator Annotation Review — Dagger_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_18`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR3 | offense | `12` | `12` |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 116 | START | 116 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 119 | START | 119 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 119 | START | 123 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 119 | START | 119 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 119 | START | 119 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 119 | START | 119 | 208 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 122 | END | 116 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR3 | `12` | `12` | 143 | START | 143 | 187 |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | `5` | `5` | 143 | START | 143 | 200 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 218 | START | 218 | 227 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_None` | 123 | 217 | 95 | inferred_complete_timeline |
| `Action_ThrowPass` | 218 | 227 | 10 | inferred_complete_timeline |
| `Action_None` | 228 | 258 | 31 | inferred_complete_timeline |
| `Action_None` | 260 | 283 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 168 | 53 | inferred_complete_timeline |
| `Action_None` | 170 | 287 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_ClearToEdge` | 143 | 200 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BreakInside` | 143 | 187 | 45 | inferred_complete_timeline |
| `Action_BreakInside` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_BreakInside` | 209 | 211 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 147 | 32 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 172 | 319 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 143 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 218 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 254 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 257 | 279 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 232 | 241 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 141 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 167 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 241 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 252 | 256 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 168 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 208 | 90 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 240 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 208 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 138 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 138 | 23 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 319 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 238 | 123 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 257 | 12 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 146 | 31 | inferred_complete_timeline |
| `Action_None` | 153 | 168 | 16 | inferred_complete_timeline |
| `Action_None` | 171 | 304 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 306 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 234 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 264 | 149 | inferred_complete_timeline |
| `Action_None` | 266 | 294 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 133–182 | 9 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 155–207 | 29 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 212–329 | 118 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 221–329 | 104 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 231–268 | 29 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 239–290 | 52 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 243–329 | 87 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 244–296 | 53 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 253–257 | 5 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 267–280 | 4 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 288–329 | 42 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BreakInside` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [116–122], lower_priority='Action_PassBlock' annotated_start=119, effective_Action_PassBlock_start=123.
- ⚠️ Action 'Action_None' range [228-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-306] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [143-200] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [143-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [189-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [209-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-218] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [257-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-238] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-141] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-182] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-241] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [245-248] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [252-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-319] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [232-241] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-168] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-226] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [242-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-302] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-329] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>