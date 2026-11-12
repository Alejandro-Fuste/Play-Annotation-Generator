# Play-Annotation-Generator Annotation Review — SplitZone_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_35`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 183
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 153
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 9 | START | 9 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 9 | START | 9 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 9 | START | 9 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 9 | START | 9 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 9 | START | 9 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 9 | START | 9 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 9 | START | 9 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 9 | START | 9 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 9 | START | 9 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 9 | START | 9 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 9 | START | 9 | 209 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 210 | START | 210 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 213 | START | 213 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 213 | START | 213 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 213 | START | 213 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 213 | START | 213 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 213 | START | 225 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `13` | `13` | 221 | START | 221 | 244 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 224 | END | 210 | 224 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 237 | START | 237 | 256 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `9` | `9` | 252 | START | 255 | 277 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `16` | `16` | 257 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–362
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_SnapReceive` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_None` | 225 | 236 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 237 | 256 | 20 | inferred_complete_timeline |
| `Action_None` | 257 | 362 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–247
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 242 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 354 | 145 | inferred_complete_timeline |
| `Action_None` | 356 | 449 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–427
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 220 | 212 | inferred_complete_timeline |
| `Action_SplitBlock` | 221 | 244 | 24 | inferred_complete_timeline |
| `Action_SplitBlock` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 306 | 306 | 1 | inferred_complete_timeline |
| `Action_None` | 308 | 340 | 33 | inferred_complete_timeline |
| `Action_None` | 358 | 427 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–281
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 212 | 204 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 236 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 251 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 266 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 281 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–249
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 212 | 204 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 235 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 249 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–277
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_BallSnap` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 231 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 255 | 277 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–282
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 212 | 204 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 234 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 251 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 262 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 282 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 212 | 204 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 250 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 288 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 306 | 449 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–281
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |
| `Action_None` | 238 | 266 | 29 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_None` | 246 | 251 | 6 | inferred_complete_timeline |
| `Action_None` | 253 | 289 | 37 | inferred_complete_timeline |
| `Action_None` | 292 | 317 | 26 | inferred_complete_timeline |
| `Action_None` | 319 | 350 | 32 | inferred_complete_timeline |
| `Action_None` | 356 | 449 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–427
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 249 | 40 | inferred_complete_timeline |
| `Action_None` | 255 | 287 | 33 | inferred_complete_timeline |
| `Action_None` | 292 | 410 | 119 | inferred_complete_timeline |
| `Action_None` | 414 | 415 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 427 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 250 | 41 | inferred_complete_timeline |
| `Action_None` | 256 | 282 | 27 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |
| `Action_None` | 320 | 350 | 31 | inferred_complete_timeline |
| `Action_None` | 358 | 364 | 7 | inferred_complete_timeline |
| `Action_None` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_None` | 374 | 421 | 48 | inferred_complete_timeline |
| `Action_None` | 425 | 430 | 6 | inferred_complete_timeline |
| `Action_None` | 432 | 445 | 14 | inferred_complete_timeline |
| `Action_None` | 449 | 449 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–281
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 270 | 61 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–281
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 253 | 44 | inferred_complete_timeline |
| `Action_None` | 255 | 281 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 313 | 104 | inferred_complete_timeline |
| `Action_None` | 319 | 339 | 21 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 353 | 381 | 29 | inferred_complete_timeline |
| `Action_None` | 387 | 449 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–284
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 284 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 9–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 209 | 201 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 84–103 | 20 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 252–449 | 124 | 13 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 256–282 | 24 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 259–446 | 165 | 9 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 312–436 | 80 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 316–440 | 125 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 320–449 | 87 | 8 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 321–344 | 22 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 321–323 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 329–341 | 13 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 333–449 | 63 | 8 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 338–449 | 75 | 5 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 345–443 | 83 | 7 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 359–449 | 89 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 376–449 | 66 | 3 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 377–449 | 69 | 4 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 385–398 | 14 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 438–442 | 5 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `9` (C): Annotated start 252 != Inferred start 255
- ❌ Missing segment for action `Action_BallCarry` on target `16` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 139 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [210–224], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=225.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=257, end=247. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 93 frames exceeds threshold 90 frames [start=213, end=305].
- ⚠️ Action 'Action_None' range [210-354] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-253] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-281] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-250] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-282] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-350] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-364] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-421] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-445] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-249] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-287] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-410] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [225-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-251] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [255-277] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-281] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-270] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [221-244] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [292-305] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 306, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [306-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-340] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-427] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-313] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-339] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-381] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-449] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-362] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-249] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-250] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [253-288] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [292-305] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-282] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-317] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-350] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-340] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-379] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-418] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-445] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-341] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-382] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-418] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-446] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-338] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-383] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-418] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-440] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-344] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-365] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-396] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-449] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-344] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-341] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-350] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-382] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-422] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-437] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-449] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-395] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-419] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-438] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-420] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-449] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-393] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-421] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-398] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '41' has 1 frames without a visible bounding box.
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