# Play-Annotation-Generator Annotation Review — DeepCross_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_89`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 209
- **Validation Warnings:** 242
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 192
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `15` | `15` | 1 | START | 1 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 4 | START | 4 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 4 | START | 4 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 4 | START | 4 | 33 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 13 | START | 13 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 13 | END | 1 | 13 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 94 | START | 94 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 163 | START | 163 | 204 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 93 | 80 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 112 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 389 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 389 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 13 | 158 | 146 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 204 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 316 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 339 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 347 | 348 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 129 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 193 | 193 | inferred_complete_timeline |
| `Action_None` | 196 | 229 | 34 | inferred_complete_timeline |
| `Action_None` | 231 | 245 | 15 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 258 | 265 | 8 | inferred_complete_timeline |
| `Action_None` | 267 | 354 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 33 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 264 | 227 | inferred_complete_timeline |
| `Action_PassBlock` | 267 | 275 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 290 | 295 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 298 | 389 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 26 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 48 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 184 | 128 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 228 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 247 | 287 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 289 | 299 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 301 | 311 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 314 | 318 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 320 | 331 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 341 | 345 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 366 | 368 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 377 | 378 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 389 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 145 | 145 | inferred_complete_timeline |
| `Action_None` | 147 | 221 | 75 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_None` | 241 | 261 | 21 | inferred_complete_timeline |
| `Action_None` | 264 | 280 | 17 | inferred_complete_timeline |
| `Action_None` | 282 | 328 | 47 | inferred_complete_timeline |
| `Action_None` | 331 | 376 | 46 | inferred_complete_timeline |
| `Action_None` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 232 | 232 | inferred_complete_timeline |
| `Action_None` | 234 | 252 | 19 | inferred_complete_timeline |
| `Action_None` | 254 | 266 | 13 | inferred_complete_timeline |
| `Action_None` | 275 | 341 | 67 | inferred_complete_timeline |
| `Action_None` | 353 | 358 | 6 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 146 | 35 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 111 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 39 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_None` | 65 | 183 | 119 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_None` | 214 | 222 | 9 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_None` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 277 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–379 | 349 | 9 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–233 | 222 | 6 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–138 | 133 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–389 | 363 | 11 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–224 | 223 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–389 | 335 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 48–88 | 8 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 68–71 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 69–339 | 249 | 8 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 80–389 | 212 | 9 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 119–142 | 24 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 181–186 | 6 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 222–228 | 7 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 236–240 | 5 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 251–305 | 47 | 5 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 261–389 | 129 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 288–333 | 22 | 5 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 290–389 | 47 | 8 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 300–310 | 11 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 305–320 | 14 | 2 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 310–314 | 5 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 324–382 | 28 | 6 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 332–350 | 19 | 1 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 355–369 | 6 | 2 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 359–363 | 5 | 1 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 359–361 | 3 | 1 | Undefined position; Undefined team |
| `49` | `58` | Position_Unknown | Team_Unknown | 366–389 | 10 | 3 | Undefined position; Undefined team |
| `50` | `59` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (15 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 169 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 92: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 92: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 92: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 92: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [163-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [277-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-286] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [323-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-129] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-124] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-241] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-309] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-341] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-367] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-233] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [267-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [279-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [290-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-252] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-341] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-358] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-145] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-261] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-280] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-328] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-376] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-114] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-160] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-330] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-111] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-354] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-228] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [238-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [247-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [289-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [301-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [314-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [320-331] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [337-338] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [341-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [366-368] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [371-373] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [377-378] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-228] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-389] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-278] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-339] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-289] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-356] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-300] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-341] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-320] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-350] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>