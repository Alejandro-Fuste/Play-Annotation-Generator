# Play-Annotation-Generator Annotation Review — InsideZoneRead_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_13`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 101
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `24` | `23` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 178 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 179 | START | 179 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 181 | START | 181 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 181 | START | 195 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `18` | 181 | START | 181 | 246 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 181 | START | 181 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `24` | `23` | 181 | START | 181 | 223 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 194 | END | 179 | 194 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 202 | START | 202 | 217 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 218 | START | 218 | 224 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `16` | 225 | START | 225 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_SnapReceive` | 179 | 194 | 16 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 202 | 217 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_None` | 225 | 247 | 23 | inferred_complete_timeline |
| `Action_None` | 255 | 271 | 17 | inferred_complete_timeline |
| `Action_None` | 273 | 345 | 73 | inferred_complete_timeline |
| `Action_None` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 213 | 35 | inferred_complete_timeline |
| `Action_None` | 215 | 359 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 246 | 66 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 223 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 246 | 14 | inferred_complete_timeline |
| `Action_None` | 247 | 256 | 10 | inferred_complete_timeline |
| `Action_None` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_BallSnap` | 179 | 194 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 280 | 20 | inferred_complete_timeline |
| `Action_None` | 285 | 310 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 246 | 66 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 210 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 246 | 27 | inferred_complete_timeline |
| `Action_None` | 247 | 257 | 11 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 315 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 229 | 51 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 287 | 37 | inferred_complete_timeline |
| `Action_None` | 289 | 293 | 5 | inferred_complete_timeline |
| `Action_None` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 274 | 96 | inferred_complete_timeline |
| `Action_None` | 276 | 359 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 321 | 143 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 292 | 114 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 338 | 160 | inferred_complete_timeline |
| `Action_None` | 340 | 355 | 16 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 356 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_None` | 179 | 275 | 97 | inferred_complete_timeline |
| `Action_None` | 277 | 302 | 26 | inferred_complete_timeline |
| `Action_None` | 306 | 338 | 33 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–357 | 316 | 9 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–54 | 34 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 28–329 | 246 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 236–241 | 6 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 247–359 | 34 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 257–359 | 54 | 8 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 281–286 | 4 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 282–359 | 78 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 300–359 | 20 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 335–340 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `24` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [179–194], lower_priority='Action_ZoneBlock' annotated_start=181, effective_Action_ZoneBlock_start=195.
- ⚠️ Action 'Action_None' range [179-315] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-338] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-355] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-271] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-345] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-275] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-302] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-359] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [217-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '11' starts at frame 195, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [195-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [230-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-280] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-292] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-321] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-356] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-336] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-346] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-38] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-338] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-316] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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