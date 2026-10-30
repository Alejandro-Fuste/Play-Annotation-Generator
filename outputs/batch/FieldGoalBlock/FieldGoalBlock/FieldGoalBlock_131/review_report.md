# Play-Annotation-Generator Annotation Review — FieldGoalBlock_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_131`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 76
- **Ball Tracks:** 0
- **Action Segments:** 299
- **Validation Warnings:** 386
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 283
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockKick` | Right_Tackle | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `16` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 48 | START | 48 | 60 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 70 | START | 70 | 76 |
| ✅ EXACT | `Action_BlockKick` | Right_Tackle | `12` | `12` | 76 | START | 76 | 95 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PlaceBall` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 161 | 77 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_KickBall` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 158 | 82 | inferred_complete_timeline |
| `Action_None` | 161 | 199 | 39 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 117 | 48 | inferred_complete_timeline |
| `Action_None` | 126 | 168 | 43 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 206 | 26 | inferred_complete_timeline |
| `Action_None` | 214 | 449 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 69 | 20 | inferred_complete_timeline |
| `Action_None` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 123 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 190 | 121 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BlockKick` | 76 | 95 | 20 | inferred_complete_timeline |
| `Action_None` | 96 | 149 | 54 | inferred_complete_timeline |
| `Action_None` | 151 | 197 | 47 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 283 | 19 | inferred_complete_timeline |
| `Action_None` | 288 | 319 | 32 | inferred_complete_timeline |
| `Action_None` | 321 | 361 | 41 | inferred_complete_timeline |
| `Action_None` | 372 | 379 | 8 | inferred_complete_timeline |
| `Action_None` | 381 | 399 | 19 | inferred_complete_timeline |
| `Action_None` | 406 | 449 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 256 | 187 | inferred_complete_timeline |
| `Action_None` | 258 | 272 | 15 | inferred_complete_timeline |
| `Action_None` | 277 | 297 | 21 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |
| `Action_None` | 333 | 375 | 43 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 246 | 177 | inferred_complete_timeline |
| `Action_None` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_None` | 263 | 293 | 31 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_None` | 300 | 305 | 6 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 338 | 17 | inferred_complete_timeline |
| `Action_None` | 356 | 358 | 3 | inferred_complete_timeline |
| `Action_None` | 370 | 372 | 3 | inferred_complete_timeline |
| `Action_None` | 394 | 395 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 388 | 319 | inferred_complete_timeline |
| `Action_None` | 395 | 399 | 5 | inferred_complete_timeline |
| `Action_None` | 402 | 410 | 9 | inferred_complete_timeline |
| `Action_None` | 417 | 449 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 344 | 275 | inferred_complete_timeline |
| `Action_None` | 349 | 364 | 16 | inferred_complete_timeline |
| `Action_None` | 368 | 449 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–394
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 117 | 48 | inferred_complete_timeline |
| `Action_None` | 120 | 183 | 64 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 209 | 10 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 247 | 33 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 266 | 271 | 6 | inferred_complete_timeline |
| `Action_None` | 273 | 297 | 25 | inferred_complete_timeline |
| `Action_None` | 300 | 359 | 60 | inferred_complete_timeline |
| `Action_None` | 362 | 366 | 5 | inferred_complete_timeline |
| `Action_None` | 368 | 394 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 70 | 208 | 139 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 247 | 20 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 379 | 115 | inferred_complete_timeline |
| `Action_None` | 406 | 432 | 27 | inferred_complete_timeline |
| `Action_None` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 202 | 90 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 271 | 202 | inferred_complete_timeline |
| `Action_None` | 273 | 283 | 11 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |
| `Action_None` | 303 | 317 | 15 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 163 | 94 | inferred_complete_timeline |
| `Action_None` | 165 | 185 | 21 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 212 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 283 | 70 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |
| `Action_None` | 304 | 317 | 14 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 24–28 | 5 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 38–56 | 14 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 45–46 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 67–449 | 342 | 10 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 93–449 | 348 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 114–443 | 265 | 15 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 120–403 | 277 | 4 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 124–449 | 313 | 6 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 132–370 | 174 | 11 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 145–190 | 40 | 3 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 154–241 | 78 | 6 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 162–445 | 205 | 19 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 193–202 | 9 | 2 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 209–215 | 7 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 238–371 | 121 | 8 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 242–449 | 190 | 5 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 265–328 | 36 | 9 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 279–449 | 169 | 2 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 280–283 | 4 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 285–287 | 3 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 287–321 | 34 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 320–344 | 12 | 4 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 334–337 | 4 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 335–354 | 14 | 3 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 343–345 | 3 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 357–449 | 92 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 359–447 | 61 | 3 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 360–362 | 3 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 363–438 | 40 | 5 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 365–366 | 2 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 367–368 | 2 | 1 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 376–378 | 3 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 379–381 | 3 | 1 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 383–385 | 3 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 386–394 | 9 | 1 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 391–449 | 54 | 3 | Undefined position; Undefined team |
| `58` | `85` | Position_Unknown | Team_Unknown | 392–406 | 15 | 1 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 397–399 | 3 | 1 | Undefined position; Undefined team |
| `61` | `88` | Position_Unknown | Team_Unknown | 407–449 | 39 | 2 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 414–415 | 2 | 1 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 420–421 | 2 | 1 | Undefined position; Undefined team |
| `65` | `93` | Position_Unknown | Team_Unknown | 425–426 | 2 | 1 | Undefined position; Undefined team |
| `66` | `94` | Position_Unknown | Team_Unknown | 431–437 | 7 | 1 | Undefined position; Undefined team |
| `67` | `95` | Position_Unknown | Team_Unknown | 432–449 | 18 | 1 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 433–437 | 5 | 1 | Undefined position; Undefined team |
| `69` | `99` | Position_Unknown | Team_Unknown | 433–449 | 17 | 1 | Undefined position; Undefined team |
| `70` | `100` | Position_Unknown | Team_Unknown | 433–449 | 12 | 2 | Undefined position; Undefined team |
| `71` | `102` | Position_Unknown | Team_Unknown | 435–440 | 6 | 1 | Undefined position; Undefined team |
| `72` | `104` | Position_Unknown | Team_Unknown | 438–449 | 12 | 1 | Undefined position; Undefined team |
| `73` | `105` | Position_Unknown | Team_Unknown | 439–440 | 2 | 1 | Undefined position; Undefined team |
| `74` | `106` | Position_Unknown | Team_Unknown | 439–446 | 8 | 1 | Undefined position; Undefined team |
| `75` | `108` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 275 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [70-246] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-293] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-338] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-185] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-283] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-317] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-256] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-329] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-375] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-388] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-410] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-206] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-247] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-394] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-344] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-364] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-158] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-208] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-247] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-379] for track '9' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-432] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-190] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-197] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-283] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-319] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-361] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-379] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-399] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-400] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-274] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-191] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-213] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-424] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-385] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-151] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-201] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-330] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-201] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-263] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-290] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-312] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-345] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-382] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-424] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-445] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-324] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-347] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-371] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-274] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-382] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-403] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-321] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-440] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-407] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-426] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-421] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-438] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-394] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-402] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-449] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-406] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-417] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-437] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-449] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-440] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-449] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.

</details>