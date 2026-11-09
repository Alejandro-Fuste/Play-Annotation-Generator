# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_80`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 165
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB2 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RT | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 403 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 266 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `15` | `15` | 223 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `16` | `16` | 223 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 223 | START | 223 | 224 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | `19` | `19` | 223 | START | 227 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 223 | START | 227 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB2 | `13` | `13` | 230 | START | 230 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RT | `19` | `19` | 247 | START | 247 | 258 |

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
- **Visible Frames:** 0–355
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 27 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 184 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 213 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 355 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 306 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 366 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 403 | 404 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 415 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 197 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 211 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 219 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 200 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 222 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 237 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 200 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 232 | 250 | 19 | inferred_complete_timeline |
| `Action_None` | 251 | 266 | 16 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 303 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 246 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 247 | 258 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 270 | 282 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_None` | 290 | 346 | 57 | inferred_complete_timeline |
| `Action_None` | 351 | 424 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 213 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 282 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 299 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 416 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 197 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 219 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 197 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 225 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 295 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 449 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 211 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 256 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 359 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 370 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 449 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 229 | 14 | inferred_complete_timeline |
| `Action_PressEdge` | 230 | 258 | 29 | inferred_complete_timeline |
| `Action_PressEdge` | 260 | 282 | 23 | inferred_complete_timeline |
| `Action_None` | 283 | 336 | 54 | inferred_complete_timeline |
| `Action_None` | 338 | 449 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 312 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 350 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 449 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 250–379 | 130 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 253–306 | 28 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 254–395 | 142 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 280–300 | 21 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 288–382 | 91 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 300–449 | 150 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 300–447 | 139 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 304–449 | 146 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 305–338 | 5 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 324–449 | 125 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 328–330 | 3 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 343–362 | 14 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 350–355 | 6 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 358–409 | 51 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 373–406 | 33 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 437–446 | 9 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (RT): Annotated start 223 != Inferred start 227
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=223, end=219. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=223, end=203. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-312] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-47] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-213] for track '2' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-282] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-416] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-197] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-225] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-295] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-449] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-403] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-415] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-366] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-211] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-256] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-370] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-449] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [230-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-336] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-197] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-200] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [239-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [245-247] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [247-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [270-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [285-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-346] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-424] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-200] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-303] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-213] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-355] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-379] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-259] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-306] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-395] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-300] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-382] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-341] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-428] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-439] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-447] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-449] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-330] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-346] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-358] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-355] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-379] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-409] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-392] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-406] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-440] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-446] for track '38' has 1 frames without a visible bounding box.
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

</details>