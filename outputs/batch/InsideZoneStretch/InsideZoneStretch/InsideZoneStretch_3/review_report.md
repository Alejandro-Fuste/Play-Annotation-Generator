# Play-Annotation-Generator Annotation Review — InsideZoneStretch_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneStretch_3`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_PressGap` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 53 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | `15` | `15` | 54 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 61 | END | 54 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 66 | START | 66 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 66 | START | 66 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 66 | START | 66 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 66 | START | 66 | 114 |
| ✅ EXACT | `Action_PressGap` | RB | `7` | `7` | 80 | START | 80 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 89 | START | 89 | 103 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `19` | `19` | 95 | START | 95 | 118 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `7` | 104 | START | 104 | 188 |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 88 | 27 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_None` | 104 | 359 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PressGap` | 80 | 103 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 188 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 154 | 101 | inferred_complete_timeline |
| `Action_None` | 156 | 343 | 188 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 359 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 239 | 186 | inferred_complete_timeline |
| `Action_None` | 242 | 359 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 94 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 95 | 118 | 24 | inferred_complete_timeline |
| `Action_None` | 119 | 251 | 133 | inferred_complete_timeline |
| `Action_None` | 253 | 285 | 33 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 335 | 11 | inferred_complete_timeline |
| `Action_None` | 337 | 343 | 7 | inferred_complete_timeline |
| `Action_None` | 346 | 356 | 11 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 114 | 34 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 136 | 359 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 114 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 359 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 114 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 177 | 63 | inferred_complete_timeline |
| `Action_None` | 179 | 258 | 80 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 267 | 359 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 114 | 49 | inferred_complete_timeline |
| `Action_None` | 115 | 253 | 139 | inferred_complete_timeline |
| `Action_None` | 255 | 260 | 6 | inferred_complete_timeline |
| `Action_None` | 265 | 288 | 24 | inferred_complete_timeline |
| `Action_None` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_None` | 337 | 341 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 359 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 90 | 37 | inferred_complete_timeline |
| `Action_None` | 92 | 301 | 210 | inferred_complete_timeline |
| `Action_None` | 303 | 309 | 7 | inferred_complete_timeline |
| `Action_None` | 315 | 359 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 312 | 259 | inferred_complete_timeline |
| `Action_None` | 316 | 326 | 11 | inferred_complete_timeline |
| `Action_None` | 329 | 335 | 7 | inferred_complete_timeline |
| `Action_None` | 341 | 349 | 9 | inferred_complete_timeline |
| `Action_None` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 162 | 109 | inferred_complete_timeline |
| `Action_None` | 165 | 263 | 99 | inferred_complete_timeline |
| `Action_None` | 268 | 306 | 39 | inferred_complete_timeline |
| `Action_None` | 311 | 325 | 15 | inferred_complete_timeline |
| `Action_None` | 334 | 338 | 5 | inferred_complete_timeline |
| `Action_None` | 340 | 343 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 170 | 117 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 190 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 359 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 359 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 312 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 359 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 359 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 267 | 214 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–121 | 122 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–359 | 359 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 125–359 | 217 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 186–189 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 189–195 | 7 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 200–208 | 9 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 202–214 | 12 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 211–359 | 149 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 224–300 | 29 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 286–359 | 74 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 310–331 | 7 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 314–328 | 15 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 315–322 | 7 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 332–341 | 10 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (QB)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 8: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 8: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [54-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-343] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-301] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-312] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-335] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-349] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-162] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-263] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-306] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-170] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [89-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-285] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-335] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-356] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-288] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-359] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-328] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-341] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>