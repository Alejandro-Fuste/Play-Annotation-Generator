# Play-Annotation-Generator Annotation Review — InsideZoneRead_194

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_194`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `23` | `22` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | CB1 | defense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | CB6 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `23` | `Group` | 0 | START | 76 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 190 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `13` | `12` | 191 | START | 191 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 194 | START | 194 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 194 | START | 194 | 236 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 194 | START | 194 | 222 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 194 | START | 194 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `23` | `22` | 194 | START | 194 | 210 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `12` | `11` | 206 | END | 191 | 206 |
| ✅ EXACT | `Action_ReadDefender` | CB1 | `12` | `11` | 211 | START | 211 | 217 |
| ✅ EXACT | `Action_Handoff` | CB1 | `12` | `11` | 218 | START | 218 | 232 |
| ✅ EXACT | `Action_BallCarry` | CB6 | `8` | `7` | 233 | START | 233 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 177 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 307 | 117 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 203 | 13 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 264 | 71 | inferred_complete_timeline |
| `Action_None` | 265 | 300 | 36 | inferred_complete_timeline |
| `Action_None` | 303 | 315 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 222 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 76–322
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 76 | 193 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 264 | 53 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |
| `Action_None` | 277 | 322 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 159 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 236 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 264 | 10 | inferred_complete_timeline |
| `Action_None` | 265 | 326 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_BallSnap` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_None` | 207 | 328 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 191 | 1 | inferred_complete_timeline |
| `Action_None` | 198 | 208 | 11 | inferred_complete_timeline |
| `Action_None` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 225 | 7 | inferred_complete_timeline |
| `Action_None` | 228 | 241 | 14 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 274 | 24 | inferred_complete_timeline |
| `Action_None` | 277 | 328 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 291 | 8 | inferred_complete_timeline |
| `Action_None` | 294 | 324 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_SnapReceive` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 218 | 232 | 15 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–329 | 316 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 4–7 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 188–230 | 43 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 190–327 | 105 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 226–253 | 28 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 269–329 | 61 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 320–322 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 388: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=194, end=159. Clamping end to start.
- ⚠️ Action 'Action_None' range [191-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 191, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [191-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-274] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-177] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-315] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-324] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-322] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '24' starts at frame 191, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [191-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_194'; source metadata written as null.

</details>