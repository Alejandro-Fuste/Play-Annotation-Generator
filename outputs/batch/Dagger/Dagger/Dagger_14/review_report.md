# Play-Annotation-Generator Annotation Review — Dagger_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_14`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 208
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `27` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `28` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `23` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `24` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `27` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `28` | `28` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `25` | `25` |
| ✅ EXACT | `Action_BreakInside` | SAF1 | defense | `15` | `15` |
| ✅ EXACT | `Action_ClearToEdge` | Position_Unknown | Team_Unknown | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `25` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 5 | START | 5 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 5 | START | 5 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 5 | START | 5 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 5 | START | 5 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `23` | `Group` | 5 | START | 5 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `24` | `Group` | 5 | START | 5 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `25` | `Group` | 5 | START | 5 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `27` | `Group` | 5 | START | 5 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `28` | `Group` | 5 | START | 5 | 186 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `19` | 184 | START | 184 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `23` | `23` | 187 | START | 187 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `24` | `24` | 187 | START | 187 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `27` | `27` | 187 | START | 187 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `28` | `28` | 187 | START | 187 | 214 |
| ✅ EXACT | `Action_SnapReceive` | QB | `25` | `25` | 188 | END | 184 | 188 |
| ✅ EXACT | `Action_BreakInside` | SAF1 | `15` | `15` | 204 | START | 204 | 329 |
| ✅ EXACT | `Action_ClearToEdge` | Position_Unknown | `4` | `4` | 204 | START | 204 | 291 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `25` | `25` | 283 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `25`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 5–259
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_SnapReceive` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 259 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–261
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 261 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–462
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 462 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 479 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–310
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 222 | 39 | inferred_complete_timeline |
| `Action_None` | 226 | 242 | 17 | inferred_complete_timeline |
| `Action_None` | 244 | 254 | 11 | inferred_complete_timeline |
| `Action_None` | 305 | 310 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `24`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 5–264
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 186 | 182 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 211 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 239 | 264 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `28`</summary>

- **xml_track_id:** `28`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 5–339
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 186 | 182 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 214 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 217 | 232 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 322 | 335 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 338 | 339 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `27`</summary>

- **xml_track_id:** `27`
- **actor_track_id:** `27`
- **team_side:** `offense`
- **Visible Frames:** 5–258
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 186 | 182 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 214 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 217 | 254 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 5–258
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 186 | 182 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 237 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 245 | 254 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–254
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 213 | 30 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_None` | 225 | 242 | 18 | inferred_complete_timeline |
| `Action_None` | 244 | 254 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 209 | 26 | inferred_complete_timeline |
| `Action_None` | 211 | 222 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–395
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 304 | 121 | inferred_complete_timeline |
| `Action_None` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 352 | 20 | inferred_complete_timeline |
| `Action_None` | 356 | 395 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–285
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 285 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 358 | 175 | inferred_complete_timeline |
| `Action_None` | 360 | 479 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–232
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 218 | 35 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–268
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 216 | 33 | inferred_complete_timeline |
| `Action_None` | 218 | 235 | 18 | inferred_complete_timeline |
| `Action_None` | 238 | 265 | 28 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `26`</summary>

- **xml_track_id:** `26`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 5–310
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 229 | 46 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 254 | 12 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 310 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–475
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 475 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 203 | 199 | inferred_complete_timeline |
| `Action_BreakInside` | 204 | 329 | 126 | inferred_complete_timeline |
| `Action_None` | 330 | 343 | 14 | inferred_complete_timeline |
| `Action_None` | 345 | 348 | 4 | inferred_complete_timeline |
| `Action_None` | 350 | 443 | 94 | inferred_complete_timeline |
| `Action_None` | 447 | 479 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–346
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 183 | 179 | inferred_complete_timeline |
| `Action_None` | 184 | 329 | 146 | inferred_complete_timeline |
| `Action_None` | 345 | 346 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–479 | 477 | 5 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 5–283 | 260 | 6 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 196–414 | 171 | 9 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 263–266 | 4 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 271–424 | 147 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 272–279 | 6 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 274–283 | 4 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 282–372 | 91 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 290–406 | 117 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 298–344 | 45 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 308–374 | 16 | 3 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 309–417 | 88 | 4 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 312–336 | 20 | 3 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 327–332 | 6 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 328–356 | 28 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 329–347 | 10 | 3 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 335–479 | 145 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 351–356 | 6 | 1 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 355–383 | 28 | 2 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 360–362 | 3 | 1 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 369–406 | 38 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 374–377 | 4 | 1 | Undefined position; Undefined team |
| `50` | `83` | Position_Unknown | Team_Unknown | 377–381 | 5 | 1 | Undefined position; Undefined team |
| `51` | `85` | Position_Unknown | Team_Unknown | 380–383 | 4 | 1 | Undefined position; Undefined team |
| `52` | `87` | Position_Unknown | Team_Unknown | 381–382 | 2 | 1 | Undefined position; Undefined team |
| `53` | `90` | Position_Unknown | Team_Unknown | 384–468 | 85 | 1 | Undefined position; Undefined team |
| `54` | `91` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |
| `55` | `92` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `56` | `95` | Position_Unknown | Team_Unknown | 418–421 | 4 | 1 | Undefined position; Undefined team |
| `57` | `96` | Position_Unknown | Team_Unknown | 421–423 | 3 | 1 | Undefined position; Undefined team |
| `58` | `100` | Position_Unknown | Team_Unknown | 456–478 | 11 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `23` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `24` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `27` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `28` (6 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `25` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 127 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 20: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '25' has invalid range: start=283, end=259. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-330] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-362] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-222] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-358] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-462] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-218] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-242] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-261] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [204-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-343] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-443] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-475] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-304] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-352] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-395] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-265] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-285] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-222] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-237] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [245-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [257-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [225-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [228-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [232-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [239-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-229] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-310] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [217-254] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [257-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [217-232] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [251-254] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [268-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [322-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [338-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-272] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-406] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-400] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-424] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-372] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-406] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-338] for track '37' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-323] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-417] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-325] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-356] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-479] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-356] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-383] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-406] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-468] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-460] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.

</details>