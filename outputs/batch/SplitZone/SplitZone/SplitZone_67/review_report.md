# Play-Annotation-Generator Annotation Review — SplitZone_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_67`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 18 | START | 19 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 18 | START | 19 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 18 | START | 19 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 18 | START | 19 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 18 | START | 19 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 18 | START | 19 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 18 | START | 19 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 18 | START | 19 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 18 | START | 19 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 18 | START | 19 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 136 | START | 136 | 152 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 139 | START | 139 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 139 | START | 153 | 190 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 139 | START | 139 | 218 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 139 | START | 139 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 139 | START | 139 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `4` | `4` | 143 | START | 143 | 193 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `21` | `21` | 151 | START | 151 | 222 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 152 | END | 136 | 152 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 155 | START | 155 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `15` | 165 | START | 165 | 169 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 222 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_SnapReceive` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 329 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 19–287
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 164 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 243 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 271 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 287 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 201 | 66 | inferred_complete_timeline |
| `Action_None` | 203 | 245 | 43 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–200
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 142 | 124 | inferred_complete_timeline |
| `Action_SplitBlock` | 143 | 193 | 51 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 19–319
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 138 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 218 | 80 | inferred_complete_timeline |
| `Action_None` | 224 | 244 | 21 | inferred_complete_timeline |
| `Action_None` | 260 | 270 | 11 | inferred_complete_timeline |
| `Action_None` | 275 | 278 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 288 | 6 | inferred_complete_timeline |
| `Action_None` | 292 | 319 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 19–328
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 138 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 151 | 222 | 72 | inferred_complete_timeline |
| `Action_None` | 223 | 328 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 19–258
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 190 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 222 | 30 | inferred_complete_timeline |
| `Action_None` | 223 | 258 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 19–264
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 138 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 222 | 84 | inferred_complete_timeline |
| `Action_None` | 223 | 242 | 20 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 19–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 138 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 222 | 84 | inferred_complete_timeline |
| `Action_None` | 223 | 259 | 37 | inferred_complete_timeline |
| `Action_None` | 261 | 267 | 7 | inferred_complete_timeline |
| `Action_None` | 269 | 273 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 225 | 90 | inferred_complete_timeline |
| `Action_None` | 227 | 244 | 18 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 19–267
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 243 | 108 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–235
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 158 | 23 | inferred_complete_timeline |
| `Action_None` | 162 | 235 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 241 | 106 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 270 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 217 | 82 | inferred_complete_timeline |
| `Action_None` | 221 | 233 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 241 | 106 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 317 | 49 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 19–327
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 319 | 184 | inferred_complete_timeline |
| `Action_None` | 325 | 327 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 329 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 19–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_None` | 136 | 230 | 95 | inferred_complete_timeline |
| `Action_None` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 19–329 | 311 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 203–271 | 49 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 211–214 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 215–219 | 5 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 259–329 | 70 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 264–329 | 58 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 266–329 | 63 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 136: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [136–152], lower_priority='Action_ZoneBlock' annotated_start=139, effective_Action_ZoneBlock_start=153.
- ⚠️ Action 'Action_None' range [136-201] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-245] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-244] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [143-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [195-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [199-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-235] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-317] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-258] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-319] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [151-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-310] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-285] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>