# Play-Annotation-Generator Annotation Review — SplitZone_276

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_276`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 109
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `7` | `7` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 100 | START | 100 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 107 | START | 107 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 107 | START | 107 | 129 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 107 | START | 117 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 107 | START | 107 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 107 | START | 107 | 108 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `7` | `7` | 110 | START | 110 | 160 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 112 | START | 112 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 116 | END | 100 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 137 | START | 137 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 147 | START | 147 | 245 |

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
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 117 | 136 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 148 | 246 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PressEdge` | 112 | 146 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 245 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 313 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 318 | 321 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 359 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 183 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 243 | 144 | inferred_complete_timeline |
| `Action_None` | 245 | 295 | 51 | inferred_complete_timeline |
| `Action_None` | 314 | 362 | 49 | inferred_complete_timeline |
| `Action_None` | 365 | 371 | 7 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 380 | 5 | inferred_complete_timeline |
| `Action_None` | 386 | 390 | 5 | inferred_complete_timeline |
| `Action_None` | 392 | 418 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 419 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_SplitBlock` | 110 | 160 | 51 | inferred_complete_timeline |
| `Action_None` | 161 | 161 | 1 | inferred_complete_timeline |
| `Action_None` | 166 | 354 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 156 | 50 | inferred_complete_timeline |
| `Action_None` | 157 | 419 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 129 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 143 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 156 | 40 | inferred_complete_timeline |
| `Action_None` | 157 | 330 | 174 | inferred_complete_timeline |
| `Action_None` | 338 | 341 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 138 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 419 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 188 | 89 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 419 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 134 | 35 | inferred_complete_timeline |
| `Action_None` | 136 | 250 | 115 | inferred_complete_timeline |
| `Action_None` | 254 | 419 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 207 | 108 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_None` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_None` | 231 | 243 | 13 | inferred_complete_timeline |
| `Action_None` | 250 | 419 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 187 | 88 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 419 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 419 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 197 | 98 | inferred_complete_timeline |
| `Action_None` | 199 | 323 | 125 | inferred_complete_timeline |
| `Action_None` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_None` | 345 | 364 | 20 | inferred_complete_timeline |
| `Action_None` | 366 | 419 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 149 | 50 | inferred_complete_timeline |
| `Action_None` | 161 | 309 | 149 | inferred_complete_timeline |
| `Action_None` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |
| `Action_None` | 328 | 383 | 56 | inferred_complete_timeline |
| `Action_None` | 392 | 394 | 3 | inferred_complete_timeline |
| `Action_None` | 397 | 400 | 4 | inferred_complete_timeline |
| `Action_None` | 406 | 419 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 200 | 101 | inferred_complete_timeline |
| `Action_None` | 202 | 251 | 50 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 362 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 277 | 178 | inferred_complete_timeline |
| `Action_None` | 279 | 419 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 300 | 201 | inferred_complete_timeline |
| `Action_None` | 303 | 397 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 118–120 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 142–419 | 258 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 156–166 | 11 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 185–419 | 206 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 204–419 | 199 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 213–419 | 142 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 365–419 | 53 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 366–419 | 54 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 379–419 | 38 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 399–419 | 17 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 407–419 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 107 != Inferred start 117
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [100–116], lower_priority='Action_ZoneBlock' annotated_start=107, effective_Action_ZoneBlock_start=117.
- ⚠️ Action 'Action_None' range [100-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-300] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-397] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-295] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-362] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-371] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-418] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-277] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 161, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [161-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-354] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-134] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-362] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-323] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [112-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-313] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [323-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-419] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-383] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [100-116] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-138] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-307] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-309] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-332] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-407] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-419] for track '33' has 1 frames without a visible bounding box.
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

</details>