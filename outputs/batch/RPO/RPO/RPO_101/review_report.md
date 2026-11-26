# Play-Annotation-Generator Annotation Review — RPO_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_101`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 192
- **Validation Warnings:** 196
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 173
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 33 | START | 33 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 33 | START | 33 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 33 | START | 38 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 33 | START | 33 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 33 | START | 33 | 34 |
| ✅ EXACT | `Action_PullBall` | RB | `4` | `4` | 37 | START | 37 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | WR3 | `1` | `1` | 38 | START | 38 | 311 |
| ✅ EXACT | `Action_ThrowPass` | RB | `4` | `4` | 69 | START | 69 | 77 |

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
- **Visible Frames:** 0–104
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 63 | 32 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_PullBall` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_ThrowPass` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 130 | 53 | inferred_complete_timeline |
| `Action_None` | 134 | 412 | 279 | inferred_complete_timeline |
| `Action_None` | 416 | 418 | 3 | inferred_complete_timeline |
| `Action_None` | 421 | 429 | 9 | inferred_complete_timeline |
| `Action_None` | 437 | 442 | 6 | inferred_complete_timeline |
| `Action_None` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 215 | 184 | inferred_complete_timeline |
| `Action_None` | 219 | 311 | 93 | inferred_complete_timeline |
| `Action_None` | 314 | 418 | 105 | inferred_complete_timeline |
| `Action_None` | 424 | 425 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 442 | 13 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 261 | 230 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 284 | 10 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 339 | 7 | inferred_complete_timeline |
| `Action_None` | 341 | 345 | 5 | inferred_complete_timeline |
| `Action_None` | 349 | 351 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 38 | 311 | 274 | inferred_complete_timeline |
| `Action_ReadDefender` | 314 | 418 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_None` | 49 | 274 | 226 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 449 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 50 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 61 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 77 | 29 | inferred_complete_timeline |
| `Action_None` | 78 | 332 | 255 | inferred_complete_timeline |
| `Action_None` | 334 | 358 | 25 | inferred_complete_timeline |
| `Action_None` | 360 | 449 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 77 | 15 | inferred_complete_timeline |
| `Action_None` | 78 | 433 | 356 | inferred_complete_timeline |
| `Action_None` | 437 | 449 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 74 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_None` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 142 | 12 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 224 | 54 | inferred_complete_timeline |
| `Action_None` | 227 | 242 | 16 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |
| `Action_None` | 278 | 287 | 10 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 449 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 77 | 45 | inferred_complete_timeline |
| `Action_None` | 78 | 149 | 72 | inferred_complete_timeline |
| `Action_None` | 154 | 351 | 198 | inferred_complete_timeline |
| `Action_None` | 354 | 449 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 56 | 25 | inferred_complete_timeline |
| `Action_None` | 79 | 103 | 25 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 277 | 160 | inferred_complete_timeline |
| `Action_None` | 282 | 286 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 115 | 84 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 188 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 58 | 18 | inferred_complete_timeline |
| `Action_None` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_None` | 72 | 78 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 91 | 60 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |
| `Action_None` | 101 | 178 | 78 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 230 | 43 | inferred_complete_timeline |
| `Action_None` | 233 | 253 | 21 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 280 | 19 | inferred_complete_timeline |
| `Action_None` | 282 | 289 | 8 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 301 | 7 | inferred_complete_timeline |
| `Action_None` | 308 | 449 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 449 | 418 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–445
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 358 | 327 | inferred_complete_timeline |
| `Action_None` | 362 | 445 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 90 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 302 | 271 | inferred_complete_timeline |
| `Action_None` | 304 | 449 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 160 | 129 | inferred_complete_timeline |
| `Action_None` | 163 | 265 | 103 | inferred_complete_timeline |
| `Action_None` | 270 | 449 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 135 | 104 | inferred_complete_timeline |
| `Action_None` | 137 | 156 | 20 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 76–449 | 374 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 94–376 | 188 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 97–449 | 330 | 7 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 113–449 | 336 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 129–267 | 109 | 6 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 199–449 | 222 | 8 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 207–220 | 6 | 3 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 209–270 | 10 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 222–236 | 5 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 226–233 | 6 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 270–449 | 180 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 300–302 | 3 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 332–449 | 118 | 1 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 339–396 | 47 | 5 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 371–372 | 2 | 1 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 149 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [32-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [38-311] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [314-418] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-230] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-280] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-449] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-412] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-429] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-442] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-274] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-215] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-311] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-418] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-442] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-63] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-433] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-90] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-449] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-265] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-358] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-445] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-351] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-58] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-188] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-97] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-224] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-287] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-449] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-277] for track '19' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 32, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [32-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-358] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-50] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-267] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-220] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-251] for track '28' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-345] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-381] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '43' has 1 frames without a visible bounding box.
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

</details>