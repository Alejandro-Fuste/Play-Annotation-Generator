# Play-Annotation-Generator Annotation Review — InsideZoneRead_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_37`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 118 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 119 | START | 119 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 121 | START | 121 | 168 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 121 | START | 121 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 121 | START | 133 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 121 | START | 121 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 121 | START | 121 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 132 | END | 119 | 132 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 136 | START | 136 | 153 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 154 | START | 154 | 161 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `7` | 162 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 136 | 153 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 419 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 232 | 114 | inferred_complete_timeline |
| `Action_None` | 234 | 255 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 299 | 181 | inferred_complete_timeline |
| `Action_None` | 321 | 327 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–404
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 375 | 257 | inferred_complete_timeline |
| `Action_None` | 398 | 404 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–400
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 386 | 268 | inferred_complete_timeline |
| `Action_None` | 388 | 400 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–398
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 198 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 230 | 25 | inferred_complete_timeline |
| `Action_None` | 231 | 291 | 61 | inferred_complete_timeline |
| `Action_None` | 297 | 318 | 22 | inferred_complete_timeline |
| `Action_None` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 364 | 3 | inferred_complete_timeline |
| `Action_None` | 366 | 398 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 230 | 110 | inferred_complete_timeline |
| `Action_None` | 231 | 337 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 230 | 98 | inferred_complete_timeline |
| `Action_None` | 231 | 331 | 101 | inferred_complete_timeline |
| `Action_None` | 351 | 357 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 150 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 230 | 72 | inferred_complete_timeline |
| `Action_None` | 231 | 419 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 168 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 230 | 58 | inferred_complete_timeline |
| `Action_None` | 231 | 354 | 124 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_None` | 417 | 419 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 261 | 143 | inferred_complete_timeline |
| `Action_None` | 263 | 276 | 14 | inferred_complete_timeline |
| `Action_None` | 302 | 312 | 11 | inferred_complete_timeline |
| `Action_None` | 331 | 419 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 244 | 126 | inferred_complete_timeline |
| `Action_None` | 252 | 272 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 159 | 41 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 200 | 19 | inferred_complete_timeline |
| `Action_None` | 204 | 419 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 192 | 74 | inferred_complete_timeline |
| `Action_None` | 206 | 285 | 80 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |
| `Action_None` | 302 | 318 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 251 | 133 | inferred_complete_timeline |
| `Action_None` | 267 | 270 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 295 | 177 | inferred_complete_timeline |
| `Action_None` | 308 | 327 | 20 | inferred_complete_timeline |
| `Action_None` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_None` | 394 | 419 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 263 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 223 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 211 | 93 | inferred_complete_timeline |
| `Action_None` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 283 | 60 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 339 | 48 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 347 | 361 | 15 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 270 | 152 | inferred_complete_timeline |
| `Action_None` | 272 | 299 | 28 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |
| `Action_None` | 364 | 375 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–291 | 292 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 155–172 | 18 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 182–263 | 73 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 187–191 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 231–419 | 185 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 251–256 | 6 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 277–286 | 6 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 296–419 | 81 | 9 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 301–419 | 73 | 7 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 313–419 | 72 | 7 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 320–342 | 8 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 371–419 | 49 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 372–419 | 48 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 374–419 | 45 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 76: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=162, end=150. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [119–132], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=133.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
- ⚠️ Action 'Action_None' range [119-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-404] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-398] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-232] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-255] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-386] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-400] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-244] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-272] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-327] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-285] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-318] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-375] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-200] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-339] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-361] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-331] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-396] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-355] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-390] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-324] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-376] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-388] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '35' has 2 frames without a visible bounding box.
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

</details>