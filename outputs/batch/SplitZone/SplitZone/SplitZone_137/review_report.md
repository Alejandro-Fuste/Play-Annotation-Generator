# Play-Annotation-Generator Annotation Review — SplitZone_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_137`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 127
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `12` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `14` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 7 | START | 8 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 7 | START | 8 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 7 | START | 8 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 7 | START | 8 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 7 | START | 8 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 7 | START | 8 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 83 | START | 83 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 85 | START | 85 | 144 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 85 | START | 93 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 85 | START | 85 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 85 | START | 85 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 85 | START | 85 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 92 | END | 83 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `21` | `21` | 110 | START | 110 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–243
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 93 | 109 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 229 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 113 | 31 | inferred_complete_timeline |
| `Action_None` | 117 | 351 | 235 | inferred_complete_timeline |
| `Action_None` | 354 | 389 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 117 | 35 | inferred_complete_timeline |
| `Action_None` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_None` | 133 | 370 | 238 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 8–353
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 192 | 110 | inferred_complete_timeline |
| `Action_None` | 194 | 253 | 60 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 347 | 84 | inferred_complete_timeline |
| `Action_None` | 349 | 353 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–188
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 188 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 389 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 108 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 144 | 13 | inferred_complete_timeline |
| `Action_None` | 145 | 389 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 8–131
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 131 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–385
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 225 | 11 | inferred_complete_timeline |
| `Action_None` | 229 | 246 | 18 | inferred_complete_timeline |
| `Action_None` | 254 | 341 | 88 | inferred_complete_timeline |
| `Action_None` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 362 | 3 | inferred_complete_timeline |
| `Action_None` | 376 | 385 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–147
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 144 | 60 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 84 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 144 | 60 | inferred_complete_timeline |
| `Action_None` | 145 | 354 | 210 | inferred_complete_timeline |
| `Action_None` | 359 | 363 | 5 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 386 | 17 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 222 | 140 | inferred_complete_timeline |
| `Action_None` | 227 | 354 | 128 | inferred_complete_timeline |
| `Action_None` | 356 | 389 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 8–384
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 326 | 244 | inferred_complete_timeline |
| `Action_None` | 328 | 384 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–300
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 131 | 49 | inferred_complete_timeline |
| `Action_None` | 133 | 295 | 163 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 125 | 43 | inferred_complete_timeline |
| `Action_None` | 127 | 389 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 235 | 153 | inferred_complete_timeline |
| `Action_None` | 241 | 253 | 13 | inferred_complete_timeline |
| `Action_None` | 259 | 389 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 180 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–354
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 152 | 70 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 261 | 354 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–241
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 199 | 117 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_None` | 235 | 241 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 285 | 203 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 331 | 25 | inferred_complete_timeline |
| `Action_None` | 334 | 338 | 5 | inferred_complete_timeline |
| `Action_None` | 346 | 389 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 389 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 82 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 240 | 158 | inferred_complete_timeline |
| `Action_None` | 242 | 253 | 12 | inferred_complete_timeline |
| `Action_None` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_None` | 266 | 389 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 112–200 | 13 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 122–381 | 237 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 153–389 | 214 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 170–174 | 5 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 188–242 | 55 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 217–389 | 167 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 230–389 | 147 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 231–389 | 159 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 236–389 | 151 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 258–314 | 48 | 6 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 281–389 | 100 | 4 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 331–389 | 12 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 85 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [83–92], lower_priority='Action_ZoneBlock' annotated_start=85, effective_Action_ZoneBlock_start=93.
- ⚠️ Action 'Action_None' range [83-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-384] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-354] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-131] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-295] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-331] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-192] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-347] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-389] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-354] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-386] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-240] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-341] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-385] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-296] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-329] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-366] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-345] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-364] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-330] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-366] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-311] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-332] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-291] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-315] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '37' has 1 frames without a visible bounding box.
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

</details>