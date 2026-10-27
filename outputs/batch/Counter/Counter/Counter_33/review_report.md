# Play-Annotation-Generator Annotation Review — Counter_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_33`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 190
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 203 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 161 | START | 161 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `17` | 171 | START | 171 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `19` | `18` | 171 | START | 176 | 228 |
| ✅ EXACT | `Action_PullBlock` | LG | `17` | `16` | 171 | START | 171 | 206 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `2` | `1` | 171 | START | 171 | 254 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 175 | END | 161 | 175 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 180 | START | 180 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 204 | START | 204 | 273 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 266 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 175 | 15 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 180 | 203 | 24 | inferred_complete_timeline |
| `Action_None` | 204 | 355 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 273 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 299 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 359 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 254 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 256 | 96 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 342 | 20 | inferred_complete_timeline |
| `Action_None` | 345 | 352 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 270 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PullBlock` | 171 | 206 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 175 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 228 | 53 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 190 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 247 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 249 | 266 | 18 | inferred_complete_timeline |
| `Action_None` | 267 | 267 | 1 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 317 | 11 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 352 | 31 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |
| `Action_None` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_None` | 284 | 293 | 10 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 270 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 216 | 56 | inferred_complete_timeline |
| `Action_None` | 221 | 229 | 9 | inferred_complete_timeline |
| `Action_None` | 250 | 272 | 23 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 290 | 7 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 192 | 32 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_None` | 242 | 249 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 277 | 117 | inferred_complete_timeline |
| `Action_None` | 281 | 313 | 33 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 229 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 245 | 85 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 261 | 8 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 258 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 287 | 127 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 170 | 10 | inferred_complete_timeline |
| `Action_None` | 173 | 237 | 65 | inferred_complete_timeline |
| `Action_None` | 239 | 266 | 28 | inferred_complete_timeline |
| `Action_None` | 278 | 290 | 13 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 299 | 311 | 13 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 261 | 101 | inferred_complete_timeline |
| `Action_None` | 267 | 270 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 332 | 48 | inferred_complete_timeline |
| `Action_None` | 335 | 359 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–84 | 43 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 229–359 | 131 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 283–359 | 77 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 283–359 | 57 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 286–347 | 59 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 290–356 | 57 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 292–326 | 32 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 300–359 | 60 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 304–327 | 12 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 304–359 | 56 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 311–326 | 11 | 3 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 312–315 | 4 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 314–359 | 40 | 3 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 314–359 | 40 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 315–358 | 44 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 315–350 | 29 | 3 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 316–359 | 17 | 6 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 328–339 | 9 | 2 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 330–332 | 3 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 346–359 | 6 | 2 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 348–350 | 3 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (RG) duration 96 frames exceeds threshold 90 frames [start=171, end=266].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (C) duration 96 frames exceeds threshold 90 frames [start=171, end=266].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [161–175], lower_priority='Action_DownBlock' annotated_start=171, effective_Action_DownBlock_start=176.
- ⚠️ Action 'Action_PullLeadBlock' range [171-254] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-270] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-256] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-342] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-352] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-273] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-216] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-287] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-258] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-266] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-290] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-332] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [171-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [249-266] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 267, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [267-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-317] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-352] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-228] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [235-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-313] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-318] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-339] for track '28' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-356] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-319] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-359] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-352] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-352] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-358] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-350] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '52' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>