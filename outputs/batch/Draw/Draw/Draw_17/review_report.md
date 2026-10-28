# Play-Annotation-Generator Annotation Review — Draw_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_17`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 190
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 143
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `24` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `24` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 55 | START | 55 | 68 |
| ✅ EXACT | `Action_PassBlock` | RT | `17` | `16` | 58 | START | 58 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `19` | 58 | START | 69 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `24` | `23` | 58 | START | 58 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `8` | `7` | 58 | START | 58 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `8` | 58 | START | 58 | 133 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `10` | `9` | 68 | END | 55 | 68 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | LB1 | `10` | `9` | 71 | START | 71 | 95 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `10` | `9` | 96 | START | 96 | 211 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 152 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 217 | 163 | inferred_complete_timeline |
| `Action_None` | 230 | 240 | 11 | inferred_complete_timeline |
| `Action_None` | 243 | 266 | 24 | inferred_complete_timeline |
| `Action_None` | 268 | 385 | 118 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 112 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 296 | 242 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 383 | 385 | 3 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 371 | 317 | inferred_complete_timeline |
| `Action_None` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 233 | 179 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 389 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 389 | 335 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 133 | 76 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 152 | 1 | inferred_complete_timeline |
| `Action_None` | 153 | 211 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 136 | 79 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 152 | 46 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 152 | 86 | inferred_complete_timeline |
| `Action_None` | 153 | 389 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 152 | 95 | inferred_complete_timeline |
| `Action_None` | 153 | 270 | 118 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 157 | 103 | inferred_complete_timeline |
| `Action_None` | 159 | 209 | 51 | inferred_complete_timeline |
| `Action_None` | 214 | 256 | 43 | inferred_complete_timeline |
| `Action_None` | 260 | 272 | 13 | inferred_complete_timeline |
| `Action_None` | 275 | 287 | 13 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 340 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 140 | 86 | inferred_complete_timeline |
| `Action_None` | 155 | 262 | 108 | inferred_complete_timeline |
| `Action_None` | 264 | 270 | 7 | inferred_complete_timeline |
| `Action_None` | 275 | 366 | 92 | inferred_complete_timeline |
| `Action_None` | 371 | 389 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 97 | 43 | inferred_complete_timeline |
| `Action_None` | 102 | 131 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 71 | 95 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 211 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 142 | 88 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 167 | 223 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 192 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 96 | 42 | inferred_complete_timeline |
| `Action_None` | 101 | 358 | 258 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 295 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 332 | 278 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 335 | 281 | inferred_complete_timeline |
| `Action_None` | 339 | 353 | 15 | inferred_complete_timeline |
| `Action_None` | 355 | 357 | 3 | inferred_complete_timeline |
| `Action_None` | 360 | 374 | 15 | inferred_complete_timeline |
| `Action_None` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 167 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–272 | 266 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–136 | 78 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 0–12 | 9 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 53–205 | 39 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 141–389 | 207 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 153–335 | 169 | 6 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 164–208 | 31 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 168–389 | 222 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 179–389 | 208 | 4 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 199–326 | 114 | 4 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 221–389 | 167 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 223–386 | 161 | 3 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 233–275 | 28 | 4 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 270–306 | 37 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 279–389 | 111 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 281–389 | 109 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 285–288 | 4 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 307–389 | 46 | 7 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 331–388 | 36 | 7 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 339–353 | 13 | 3 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 345–389 | 41 | 2 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 349–389 | 41 | 1 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 358–389 | 32 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 360–389 | 29 | 2 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 377–381 | 5 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 384–387 | 4 | 1 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `24` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 129 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_PassBlock' annotated_start=58, effective_Action_PassBlock_start=69.
- ⚠️ Action 'Action_None' range [55-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-262] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-366] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-358] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-211] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-296] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-335] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-353] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-374] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-371] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-266] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-385] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-270] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-142] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-332] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-136] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-8] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-63] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-205] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-330] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-389] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-329] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-300] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-382] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-253] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-306] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-340] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-346] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-383] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-389] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-386] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'Draw_17'; source metadata written as null.

</details>