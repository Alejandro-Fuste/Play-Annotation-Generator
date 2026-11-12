# Play-Annotation-Generator Annotation Review — SplitZone_306

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_306`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 12
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_BallSnap` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `19` | `19` |
| ✅ EXACT | `Action_PressEdge` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ReadEdgeDefender` | DT1 | defense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | DT1 | defense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | DT1 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 171 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 81 | START | 81 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 81 | START | 81 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 81 | START | 81 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 81 | START | 81 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 81 | START | 81 | 226 |
| ✅ EXACT | `Action_BallSnap` | WR1 | `3` | `3` | 172 | START | 172 | 183 |
| ✅ EXACT | `Action_SplitBlock` | TE | `4` | `4` | 179 | START | 179 | 217 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `19` | `19` | 185 | END | 172 | 185 |
| ✅ EXACT | `Action_PressEdge` | RT | `13` | `13` | 192 | START | 192 | 248 |
| ✅ EXACT | `Action_ReadEdgeDefender` | DT1 | `19` | `19` | 193 | START | 193 | 205 |
| ✅ EXACT | `Action_BallCarry` | DT1 | `19` | `19` | 217 | START | 217 | 217 |
| ✅ EXACT | `Action_Handoff` | DT1 | `19` | `19` | 218 | START | 218 | 378 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 204 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 232 | 29 | inferred_complete_timeline |
| `Action_None` | 234 | 257 | 24 | inferred_complete_timeline |
| `Action_None` | 265 | 332 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 227 | 56 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 261 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_SplitBlock` | 179 | 217 | 39 | inferred_complete_timeline |
| `Action_None` | 218 | 374 | 157 | inferred_complete_timeline |
| `Action_None` | 377 | 389 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 226 | 146 | inferred_complete_timeline |
| `Action_None` | 227 | 307 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 226 | 146 | inferred_complete_timeline |
| `Action_None` | 227 | 331 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 226 | 146 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 226 | 146 | inferred_complete_timeline |
| `Action_None` | 227 | 389 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 191 | 111 | inferred_complete_timeline |
| `Action_PressEdge` | 192 | 248 | 57 | inferred_complete_timeline |
| `Action_None` | 249 | 389 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 278 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_None` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 218 | 378 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 298 | 127 | inferred_complete_timeline |
| `Action_None` | 308 | 389 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 218 | 47 | inferred_complete_timeline |
| `Action_None` | 220 | 312 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 358 | 187 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–35 | 33 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 22–72 | 36 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 52–229 | 27 | 6 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 65–72 | 8 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 93–96 | 4 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 209–271 | 59 | 4 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 237–301 | 65 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 266–338 | 73 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 276–318 | 43 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 282–308 | 27 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 294–389 | 96 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 313–330 | 11 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 329–363 | 24 | 4 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 333–370 | 15 | 3 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 347–354 | 7 | 2 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 380–389 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
- ⚠️ Action 'Action_None' range [172-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-307] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [172-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-257] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-332] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-358] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [218-378] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-16] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-35] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-35] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-56] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-72] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-96] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-301] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-338] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-320] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-342] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-351] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '46' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>