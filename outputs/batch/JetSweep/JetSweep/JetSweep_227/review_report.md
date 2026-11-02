# Play-Annotation-Generator Annotation Review — JetSweep_227

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_227`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 208
- **Validation Warnings:** 214
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 183
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 27 | START | 27 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 42 | START | 42 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 43 | START | 43 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 43 | START | 43 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 43 | START | 43 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 43 | START | 73 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 43 | START | 43 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `1` | `0` | 63 | START | 63 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 72 | END | 42 | 72 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 80 | START | 80 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `1` | 88 | START | 88 | 226 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_Toss` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 305 | 218 | inferred_complete_timeline |
| `Action_None` | 308 | 405 | 98 | inferred_complete_timeline |
| `Action_None` | 407 | 449 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 230 | 189 | inferred_complete_timeline |
| `Action_None` | 233 | 268 | 36 | inferred_complete_timeline |
| `Action_None` | 288 | 449 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–414
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_JetMotion` | 27 | 87 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 226 | 139 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 291 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 414 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 275 | 234 | inferred_complete_timeline |
| `Action_None` | 277 | 302 | 26 | inferred_complete_timeline |
| `Action_None` | 305 | 449 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 91 | 186 | 96 | inferred_complete_timeline |
| `Action_None` | 188 | 255 | 68 | inferred_complete_timeline |
| `Action_None` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 449 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_LeadBlock` | 63 | 88 | 26 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 162 | 72 | inferred_complete_timeline |
| `Action_LeadBlock` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 178 | 178 | 1 | inferred_complete_timeline |
| `Action_None` | 180 | 192 | 13 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_None` | 212 | 423 | 212 | inferred_complete_timeline |
| `Action_None` | 426 | 449 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 80 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 86 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 177 | 90 | inferred_complete_timeline |
| `Action_None` | 178 | 236 | 59 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 298 | 13 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 449 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 177 | 86 | inferred_complete_timeline |
| `Action_None` | 178 | 230 | 53 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 240 | 248 | 9 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 291 | 10 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 315 | 10 | inferred_complete_timeline |
| `Action_None` | 317 | 449 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 85 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 108 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 86 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 180 | 139 | inferred_complete_timeline |
| `Action_None` | 182 | 197 | 16 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 247 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 85 | 44 | inferred_complete_timeline |
| `Action_None` | 95 | 198 | 104 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 230 | 28 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 264 | 267 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 89 | 226 | 138 | inferred_complete_timeline |
| `Action_None` | 253 | 261 | 9 | inferred_complete_timeline |
| `Action_None` | 263 | 268 | 6 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 281 | 449 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 199 | 158 | inferred_complete_timeline |
| `Action_None` | 207 | 449 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 302 | 261 | inferred_complete_timeline |
| `Action_None` | 305 | 449 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 269 | 228 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 301 | 8 | inferred_complete_timeline |
| `Action_None` | 307 | 331 | 25 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 410 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 192 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 92 | 123 | 32 | inferred_complete_timeline |
| `Action_None` | 129 | 267 | 139 | inferred_complete_timeline |
| `Action_None` | 269 | 278 | 10 | inferred_complete_timeline |
| `Action_None` | 280 | 301 | 22 | inferred_complete_timeline |
| `Action_None` | 303 | 309 | 7 | inferred_complete_timeline |
| `Action_None` | 316 | 327 | 12 | inferred_complete_timeline |
| `Action_None` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 449 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–439
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 186 | 145 | inferred_complete_timeline |
| `Action_None` | 188 | 231 | 44 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 268 | 12 | inferred_complete_timeline |
| `Action_None` | 273 | 411 | 139 | inferred_complete_timeline |
| `Action_None` | 419 | 439 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 224 | 183 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 250 | 373 | 124 | inferred_complete_timeline |
| `Action_None` | 376 | 378 | 3 | inferred_complete_timeline |
| `Action_None` | 382 | 449 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 96–230 | 135 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 98–314 | 212 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 105–124 | 20 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 125–449 | 311 | 7 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 219–449 | 231 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 235–449 | 199 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 254–449 | 162 | 5 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 255–449 | 166 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 261–374 | 106 | 6 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 262–266 | 5 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 271–449 | 113 | 13 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 310–449 | 133 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 313–365 | 25 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 338–437 | 100 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 362–392 | 28 | 4 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 364–374 | 6 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 372–399 | 26 | 2 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 397–412 | 5 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 411–420 | 9 | 2 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 165 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '0' (TE2) duration 115 frames exceeds threshold 90 frames [start=63, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 135 frames exceeds threshold 90 frames [start=43, end=177].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 135 frames exceeds threshold 90 frames [start=43, end=177].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [42–72], lower_priority='Action_ZoneBlock' annotated_start=43, effective_Action_ZoneBlock_start=73.
- ⚠️ Action 'Action_LeadBlock' range [63-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-162] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [168-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '0' starts at frame 178, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [178-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-423] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-250] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-300] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-414] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-302] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-230] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-449] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-255] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-239] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-405] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-198] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-449] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-267] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-301] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-411] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-439] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-331] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-410] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-373] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [42-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-230] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-314] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-338] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-259] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-273] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-302] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-366] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-297] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-368] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-320] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-363] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-376] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-349] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-437] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-392] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-393] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '41' has 2 frames without a visible bounding box.
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

</details>