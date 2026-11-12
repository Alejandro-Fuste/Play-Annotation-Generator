# Play-Annotation-Generator Annotation Review — SplitZone_226

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_226`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 12 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 74 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 145 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 143 | START | 143 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 146 | START | 162 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 146 | START | 146 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 146 | START | 146 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 146 | START | 146 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 146 | START | 146 | 156 |
| ✅ EXACT | `Action_SplitBlock` | TE | `6` | `6` | 149 | START | 149 | 149 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `0` | `0` | 157 | END | 143 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `0` | `0` | 163 | START | 163 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 172 | START | 172 | 173 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `14` | `14` | 183 | START | 183 | 263 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 263 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 260 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 213 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 256 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 397 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 399 | 408 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_SplitBlock` | 149 | 149 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 156 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 160 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 182 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 263 | 53 | inferred_complete_timeline |
| `Action_None` | 264 | 419 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–419
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 142 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 263 | 49 | inferred_complete_timeline |
| `Action_None` | 264 | 419 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 74–419
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 74 | 145 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 166 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 182 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 183 | 263 | 81 | inferred_complete_timeline |
| `Action_None` | 264 | 419 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 182 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 240 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_None` | 264 | 320 | 57 | inferred_complete_timeline |
| `Action_None` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 419 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–402
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 197 | 55 | inferred_complete_timeline |
| `Action_None` | 223 | 402 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_None` | 191 | 203 | 13 | inferred_complete_timeline |
| `Action_None` | 211 | 326 | 116 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_None` | 341 | 356 | 16 | inferred_complete_timeline |
| `Action_None` | 358 | 377 | 20 | inferred_complete_timeline |
| `Action_None` | 380 | 419 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 46 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 138 | 79 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 409 | 199 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 142 | 43 | inferred_complete_timeline |
| `Action_None` | 143 | 143 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 170 | 26 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 262 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 218 | 76 | inferred_complete_timeline |
| `Action_None` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_None` | 245 | 259 | 15 | inferred_complete_timeline |
| `Action_None` | 262 | 419 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 142 | 128 | inferred_complete_timeline |
| `Action_None` | 143 | 245 | 103 | inferred_complete_timeline |
| `Action_None` | 252 | 266 | 15 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 338 | 21 | inferred_complete_timeline |
| `Action_None` | 346 | 364 | 19 | inferred_complete_timeline |
| `Action_None` | 366 | 377 | 12 | inferred_complete_timeline |
| `Action_None` | 379 | 387 | 9 | inferred_complete_timeline |
| `Action_None` | 391 | 419 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 173–419 | 225 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 181–203 | 19 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 183–419 | 233 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 185–419 | 235 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 211–215 | 5 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 212–419 | 208 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 222–419 | 193 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 274–418 | 135 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 275–296 | 22 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 319–363 | 45 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 327–419 | 79 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 330–408 | 64 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 346–347 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 358–417 | 45 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 385–386 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 388–415 | 25 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 127 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [143–157], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=158.
- ⚠️ Action 'Action_SnapReceive' range [143-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [163-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [168-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 143, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [143-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-262] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-402] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [245-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-419] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' for track '6' starts at frame 149, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SplitBlock' range [149-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-46] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-409] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-213] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-397] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [399-408] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-338] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-364] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-377] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-387] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-326] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-377] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [143-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-203] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-419] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-366] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-397] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-418] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-296] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-363] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-366] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-384] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-408] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-385] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-402] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-417] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-409] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>