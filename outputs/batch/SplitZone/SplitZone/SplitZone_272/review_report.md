# Play-Annotation-Generator Annotation Review — SplitZone_272

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_272`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 187
- **Validation Warnings:** 182
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 166
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 112 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 77 | START | 77 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `4` | `4` | 83 | START | 83 | 121 |
| ✅ EXACT | `Action_SnapReceive` | WR2 | `2` | `2` | 85 | END | 77 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 92 | START | 92 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 92 | START | 92 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 92 | START | 92 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | C | `5` | `5` | 92 | START | 92 | 113 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 94 | START | 94 | 131 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 113 | START | 113 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 132 | START | 132 | 151 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `5` | `5` | 135 | START | 135 | 145 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 133 | 21 | inferred_complete_timeline |
| `Action_None` | 134 | 251 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PressEdge` | 94 | 131 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 151 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 169 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 389 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 303 | 218 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 316 | 4 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 106 | 30 | inferred_complete_timeline |
| `Action_None` | 110 | 306 | 197 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |
| `Action_None` | 314 | 389 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SplitBlock` | 83 | 121 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |
| `Action_None` | 159 | 389 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 110 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 161 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 113 | 22 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 146 | 174 | 29 | inferred_complete_timeline |
| `Action_None` | 176 | 185 | 10 | inferred_complete_timeline |
| `Action_None` | 188 | 283 | 96 | inferred_complete_timeline |
| `Action_None` | 288 | 302 | 15 | inferred_complete_timeline |
| `Action_None` | 317 | 320 | 4 | inferred_complete_timeline |
| `Action_None` | 322 | 330 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 113 | 22 | inferred_complete_timeline |
| `Action_None` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 141 | 19 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 156 | 166 | 11 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 219 | 32 | inferred_complete_timeline |
| `Action_None` | 238 | 284 | 47 | inferred_complete_timeline |
| `Action_None` | 288 | 308 | 21 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 113 | 22 | inferred_complete_timeline |
| `Action_None` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_None` | 124 | 247 | 124 | inferred_complete_timeline |
| `Action_None` | 249 | 330 | 82 | inferred_complete_timeline |
| `Action_None` | 333 | 342 | 10 | inferred_complete_timeline |
| `Action_None` | 344 | 346 | 3 | inferred_complete_timeline |
| `Action_None` | 348 | 353 | 6 | inferred_complete_timeline |
| `Action_None` | 355 | 357 | 3 | inferred_complete_timeline |
| `Action_None` | 361 | 367 | 7 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 141 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 190 | 47 | inferred_complete_timeline |
| `Action_None` | 195 | 225 | 31 | inferred_complete_timeline |
| `Action_None` | 227 | 284 | 58 | inferred_complete_timeline |
| `Action_None` | 287 | 303 | 17 | inferred_complete_timeline |
| `Action_None` | 317 | 389 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 121 | 45 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 121 | 45 | inferred_complete_timeline |
| `Action_None` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_None` | 143 | 246 | 104 | inferred_complete_timeline |
| `Action_None` | 248 | 283 | 36 | inferred_complete_timeline |
| `Action_None` | 288 | 302 | 15 | inferred_complete_timeline |
| `Action_None` | 317 | 320 | 4 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 155 | 174 | 20 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 283 | 95 | inferred_complete_timeline |
| `Action_None` | 287 | 303 | 17 | inferred_complete_timeline |
| `Action_None` | 305 | 310 | 6 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 332 | 7 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_None` | 364 | 368 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 283 | 116 | inferred_complete_timeline |
| `Action_None` | 287 | 321 | 35 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 337 | 8 | inferred_complete_timeline |
| `Action_None` | 349 | 361 | 13 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 136 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 389 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 149 | 73 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 247 | 93 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 389 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 141 | 65 | inferred_complete_timeline |
| `Action_None` | 143 | 284 | 142 | inferred_complete_timeline |
| `Action_None` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 316 | 328 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 389 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 313 | 237 | inferred_complete_timeline |
| `Action_None` | 317 | 334 | 18 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |
| `Action_None` | 361 | 368 | 8 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–389 | 389 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 18–117 | 83 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 161–188 | 15 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 189–389 | 190 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 199–221 | 10 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 203–389 | 173 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 213–219 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 217–388 | 171 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 220–245 | 26 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 221–318 | 98 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 283–320 | 24 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 284–319 | 26 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 285–296 | 11 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 368–379 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 146 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 546: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [77-141] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-328] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-110] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-303] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-190] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [83-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-174] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-283] for track '5' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-302] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-306] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-283] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-337] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-361] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-251] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-313] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-334] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-368] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-373] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-116] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-283] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-136] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-121] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-121] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-246] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-283] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-247] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-141] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-219] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-284] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-308] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-247] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-330] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-40] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-338] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-370] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-379] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-245] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-318] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-293] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-313] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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