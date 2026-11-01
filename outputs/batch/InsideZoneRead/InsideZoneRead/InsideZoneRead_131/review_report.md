# Play-Annotation-Generator Annotation Review — InsideZoneRead_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_131`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 103 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 154 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 155 | START | 155 | 168 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 158 | START | 169 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 158 | START | 158 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 158 | START | 158 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 158 | START | 158 | 173 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `20` | 158 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 168 | END | 155 | 168 |
| ✅ EXACT | `Action_ReadDefender` | QB | `22` | `21` | 172 | START | 172 | 185 |
| ✅ EXACT | `Action_BallCarry` | RB | `11` | `10` | 175 | START | 175 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `22` | `21` | 186 | START | 186 | 268 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | C | `12` | `11` | 200 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 103–389
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 154 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 155 | 168 | 14 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 172 | 185 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 186 | 268 | 83 | inferred_complete_timeline |
| `Action_Handoff` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 278 | 331 | 54 | inferred_complete_timeline |
| `Action_Handoff` | 333 | 389 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 177 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 389 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 389 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 267 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 154 | 128 | inferred_complete_timeline |
| `Action_None` | 155 | 389 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 157 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 173 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 229 | 30 | inferred_complete_timeline |
| `Action_None` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_None` | 284 | 389 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 5 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 21 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BallSnap` | 155 | 168 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 169 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 103 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 157 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 169 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 157 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 174 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 199 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 97 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 154 | 55 | inferred_complete_timeline |
| `Action_None` | 155 | 195 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 130 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 154 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 199 | 45 | inferred_complete_timeline |
| `Action_None` | 201 | 267 | 67 | inferred_complete_timeline |
| `Action_None` | 277 | 287 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 304 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 32 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 154 | 105 | inferred_complete_timeline |
| `Action_None` | 155 | 181 | 27 | inferred_complete_timeline |
| `Action_None` | 207 | 261 | 55 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 389 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 103 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 154 | 49 | inferred_complete_timeline |
| `Action_None` | 155 | 189 | 35 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 261 | 49 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 291 | 7 | inferred_complete_timeline |
| `Action_None` | 297 | 307 | 11 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 331 | 11 | inferred_complete_timeline |
| `Action_None` | 337 | 343 | 7 | inferred_complete_timeline |
| `Action_None` | 348 | 358 | 11 | inferred_complete_timeline |
| `Action_None` | 370 | 377 | 8 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 154 | 106 | inferred_complete_timeline |
| `Action_None` | 155 | 207 | 53 | inferred_complete_timeline |
| `Action_None` | 211 | 243 | 33 | inferred_complete_timeline |
| `Action_None` | 291 | 308 | 18 | inferred_complete_timeline |
| `Action_None` | 320 | 389 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 154 | 75 | inferred_complete_timeline |
| `Action_None` | 155 | 190 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 378 | 224 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 284 | 130 | inferred_complete_timeline |
| `Action_None` | 301 | 309 | 9 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 389 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 250 | 96 | inferred_complete_timeline |
| `Action_None` | 255 | 262 | 8 | inferred_complete_timeline |
| `Action_None` | 264 | 270 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 313 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 163–389 | 194 | 8 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 190–218 | 29 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 218–239 | 21 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 218–255 | 36 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 234–242 | 9 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 274–389 | 115 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 274–282 | 9 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 278–389 | 103 | 5 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 279–389 | 104 | 8 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 284–389 | 98 | 7 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 301–342 | 37 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 302–384 | 78 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 304–389 | 80 | 3 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 321–389 | 64 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 328–387 | 39 | 6 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 334–389 | 41 | 2 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 342–389 | 48 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 353–389 | 35 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 364–366 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 158 != Inferred start 169
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `22` (4 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `12` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 141 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '11' has invalid range: start=200, end=169. Clamping end to start.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [155–168], lower_priority='Action_ZoneBlock' annotated_start=158, effective_Action_ZoneBlock_start=169.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=158, end=21. Clamping end to start.
- ⚠️ Action 'Action_None' range [155-378] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-389] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-313] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-31] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-199] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-308] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '11' starts at frame 169, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [169-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-195] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-103] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-189] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-261] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-331] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-358] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-377] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [200-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-32] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-41] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-181] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-261] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-21] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [186-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [271-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [278-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-204] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-328] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-218] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-235] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-389] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-303] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-316] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-332] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-306] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-317] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-333] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-376] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-387] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-359] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-331] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-331] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-384] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-325] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-372] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-373] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '41' has 1 frames without a visible bounding box.
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

</details>