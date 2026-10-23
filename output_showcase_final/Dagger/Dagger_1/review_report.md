# Play-Annotation-Generator Annotation Review — Dagger_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_1`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 160 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 158 | START | 158 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 161 | START | 175 | 242 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 161 | START | 161 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 161 | START | 161 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `3` | 161 | START | 161 | 252 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `8` | `8` | 161 | START | 161 | 291 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `0` | `0` | 174 | START | 174 | 297 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `1` | `1` | 174 | START | 174 | 256 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 174 | END | 158 | 174 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 246 | START | 246 | 259 |

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
- **Visible Frames:** 0–314
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_SnapReceive` | 158 | 174 | 17 | inferred_complete_timeline |
| `Action_None` | 175 | 245 | 71 | inferred_complete_timeline |
| `Action_ThrowPass` | 246 | 259 | 14 | inferred_complete_timeline |
| `Action_None` | 260 | 268 | 9 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 314 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 389 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ClearToEdge` | 174 | 256 | 83 | inferred_complete_timeline |
| `Action_None` | 257 | 278 | 22 | inferred_complete_timeline |
| `Action_None` | 280 | 377 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_BreakInside` | 174 | 297 | 124 | inferred_complete_timeline |
| `Action_None` | 298 | 332 | 35 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 360 | 24 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 389 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 187 | 30 | inferred_complete_timeline |
| `Action_None` | 196 | 389 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 252 | 92 | inferred_complete_timeline |
| `Action_PassBlock` | 256 | 267 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 283 | 290 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 296 | 314 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 339 | 340 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 291 | 131 | inferred_complete_timeline |
| `Action_PassBlock` | 293 | 315 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 174 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 242 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 250 | 266 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 284 | 301 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 308 | 310 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 203 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 186 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 198 | 385 | 188 | inferred_complete_timeline |
| `Action_PassBlock` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 242 | 85 | inferred_complete_timeline |
| `Action_None` | 244 | 252 | 9 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 250 | 93 | inferred_complete_timeline |
| `Action_None` | 252 | 289 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 174 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 272 | 97 | inferred_complete_timeline |
| `Action_None` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 381 | 224 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 293 | 136 | inferred_complete_timeline |
| `Action_None` | 297 | 389 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 234 | 77 | inferred_complete_timeline |
| `Action_None` | 236 | 260 | 25 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 368 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 372 | 215 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 389 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 337 | 180 | inferred_complete_timeline |
| `Action_None` | 340 | 351 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 331 | 174 | inferred_complete_timeline |
| `Action_None` | 334 | 349 | 16 | inferred_complete_timeline |
| `Action_None` | 352 | 379 | 28 | inferred_complete_timeline |
| `Action_None` | 382 | 388 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 202–335 | 123 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 235–389 | 92 | 6 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 250–389 | 102 | 9 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 299–315 | 17 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 306–386 | 13 | 3 | Undefined position; Undefined team |
| `28` | `49` | Position_Unknown | Team_Unknown | 327–340 | 12 | 2 | Undefined position; Undefined team |
| `29` | `51` | Position_Unknown | Team_Unknown | 331–368 | 5 | 2 | Undefined position; Undefined team |
| `30` | `54` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `31` | `57` | Position_Unknown | Team_Unknown | 354–356 | 3 | 1 | Undefined position; Undefined team |
| `32` | `58` | Position_Unknown | Team_Unknown | 358–389 | 23 | 3 | Undefined position; Undefined team |
| `33` | `62` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `34` | `64` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |
| `35` | `65` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [158–174], lower_priority='Action_PassBlock' annotated_start=161, effective_Action_PassBlock_start=175.
- ⚠️ Action 'Action_BreakInside' range [174-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-332] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-360] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-377] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [256-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [270-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [276-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [283-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [293-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [296-314] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [332-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [339-340] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-242] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-368] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-337] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-351] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-349] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-379] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-388] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-291] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [293-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [324-325] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-234] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-242] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [245-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [250-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [270-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [276-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [281-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [284-301] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [308-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-372] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-293] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-389] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-314] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-381] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-272] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-250] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-289] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-203] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-186] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [198-385] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-321] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-321] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-333] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-353] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-369] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-315] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-369] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '35' has 1 frames without a visible bounding box.
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