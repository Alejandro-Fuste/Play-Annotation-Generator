# Play-Annotation-Generator Annotation Review — SplitZone_296

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_296`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 41 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 171 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 172 | START | 172 | 185 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `2` | `2` | 181 | START | 181 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 182 | START | 182 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 182 | START | 182 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 182 | START | 182 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `22` | 182 | START | 182 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 182 | START | 186 | 191 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 185 | START | 185 | 212 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 185 | END | 172 | 185 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `14` | `14` | 193 | START | 193 | 205 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 206 | START | 206 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 213 | START | 213 | 263 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `20` | `20` | 215 | START | 215 | 253 |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 193 | 205 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_None` | 217 | 359 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PressEdge` | 185 | 212 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 263 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 326 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_SplitBlock` | 181 | 214 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 197 | 26 | inferred_complete_timeline |
| `Action_None` | 263 | 359 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 41–359
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 181 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 207 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 229 | 20 | inferred_complete_timeline |
| `Action_None` | 230 | 293 | 64 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 201 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 214 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 215 | 253 | 39 | inferred_complete_timeline |
| `Action_None` | 254 | 359 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 229 | 26 | inferred_complete_timeline |
| `Action_None` | 230 | 359 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 199 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 229 | 1 | inferred_complete_timeline |
| `Action_None` | 230 | 251 | 22 | inferred_complete_timeline |
| `Action_None` | 254 | 302 | 49 | inferred_complete_timeline |
| `Action_None` | 305 | 359 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 229 | 48 | inferred_complete_timeline |
| `Action_None` | 230 | 254 | 25 | inferred_complete_timeline |
| `Action_None` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 305 | 134 | inferred_complete_timeline |
| `Action_None` | 309 | 359 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 216 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |
| `Action_None` | 201 | 262 | 62 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 290 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 237 | 66 | inferred_complete_timeline |
| `Action_None` | 250 | 267 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 278 | 107 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 316 | 145 | inferred_complete_timeline |
| `Action_None` | 319 | 323 | 5 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 344 | 173 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 298 | 127 | inferred_complete_timeline |
| `Action_None` | 302 | 359 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 338 | 167 | inferred_complete_timeline |
| `Action_None` | 341 | 359 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 158 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 171 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 13–147 | 122 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 219–270 | 41 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 222–359 | 128 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 239–359 | 121 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 268–341 | 57 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 283–359 | 75 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 324–332 | 9 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [172–185], lower_priority='Action_ZoneBlock' annotated_start=182, effective_Action_ZoneBlock_start=186.
- ⚠️ Action 'Action_SplitBlock' range [181-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-316] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-359] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-262] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-305] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-326] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [333-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-344] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-338] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-359] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-185] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-199] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-217] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-302] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-201] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-116] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-312] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-345] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '30' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>