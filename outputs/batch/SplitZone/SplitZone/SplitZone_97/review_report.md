# Play-Annotation-Generator Annotation Review — SplitZone_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_97`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 157 |
| ✅ EXACT | `Action_BallSnap` | RG | `19` | `19` | 153 | START | 153 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 156 | START | 156 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `17` | 156 | START | 156 | 228 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 156 | START | 156 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 156 | START | 156 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 156 | START | 156 | 201 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `7` | `7` | 158 | START | 158 | 221 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 165 | END | 153 | 165 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 170 | START | 170 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `19` | `19` | 175 | START | 175 | 221 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 180 | START | 180 | 325 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 228 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SnapReceive` | 153 | 165 | 13 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 170 | 179 | 10 | inferred_complete_timeline |
| `Action_None` | 180 | 359 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 325 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 359 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 293 | 141 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_SplitBlock` | 158 | 221 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 185 | 33 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 267 | 77 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 290 | 18 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 320 | 23 | inferred_complete_timeline |
| `Action_None` | 322 | 359 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 228 | 73 | inferred_complete_timeline |
| `Action_None` | 229 | 271 | 43 | inferred_complete_timeline |
| `Action_None` | 274 | 291 | 18 | inferred_complete_timeline |
| `Action_None` | 294 | 318 | 25 | inferred_complete_timeline |
| `Action_None` | 325 | 359 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 228 | 73 | inferred_complete_timeline |
| `Action_None` | 229 | 268 | 40 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 359 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 201 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 219 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_None` | 236 | 255 | 20 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_BallSnap` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 174 | 19 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 175 | 221 | 47 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 264 | 36 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 303 | 30 | inferred_complete_timeline |
| `Action_None` | 305 | 359 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 169 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 228 | 52 | inferred_complete_timeline |
| `Action_None` | 229 | 254 | 26 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 268 | 116 | inferred_complete_timeline |
| `Action_None` | 273 | 290 | 18 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 268 | 116 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 290 | 18 | inferred_complete_timeline |
| `Action_None` | 297 | 318 | 22 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 188 | 36 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 267 | 45 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 293 | 19 | inferred_complete_timeline |
| `Action_None` | 297 | 303 | 7 | inferred_complete_timeline |
| `Action_None` | 305 | 317 | 13 | inferred_complete_timeline |
| `Action_None` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 359 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 211 | 59 | inferred_complete_timeline |
| `Action_None` | 213 | 267 | 55 | inferred_complete_timeline |
| `Action_None` | 274 | 293 | 20 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 204 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 302 | 150 | inferred_complete_timeline |
| `Action_None` | 304 | 334 | 31 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 337 | 185 | inferred_complete_timeline |
| `Action_None` | 340 | 359 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 355 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 290 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 205–215 | 10 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 219–229 | 11 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 227–359 | 52 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 239–318 | 47 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 251–260 | 9 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 275–359 | 79 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 286–290 | 5 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 287–359 | 56 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 299–317 | 18 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 304–359 | 41 | 4 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 306–359 | 45 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 309–320 | 12 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 328–359 | 25 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 338–348 | 10 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 101 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [153-293] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-325] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-355] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [158-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-267] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-228] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-267] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-337] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-359] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-271] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-334] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [175-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-303] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-359] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [214-219] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [221-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-255] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-252] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-318] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-303] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-320] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '37' has 1 frames without a visible bounding box.
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