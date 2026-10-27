# Play-Annotation-Generator Annotation Review — Counter_151

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_151`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 244
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 173
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `29` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `29` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `24` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `29` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `1` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 7 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `24` | `Group` | 0 | START | 42 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `29` | `Group` | 0 | START | 108 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 212 |
| ✅ EXACT | `Action_BallSnap` | RG | `29` | `21` | 213 | START | 213 | 215 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 215 | END | 213 | 215 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `12` | 218 | START | 218 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `24` | `18` | 218 | START | 218 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `29` | `21` | 218 | START | 226 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `16` | 218 | START | 218 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `16` | `15` | 218 | START | 218 | 221 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 239 | START | 239 | 255 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 256 | START | 256 | 334 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 307 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 212 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 238 | 23 | inferred_complete_timeline |
| `Action_Handoff` | 239 | 255 | 17 | inferred_complete_timeline |
| `Action_None` | 256 | 449 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 334 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 360 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 396 | 425 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 427 | 449 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 263 | 51 | inferred_complete_timeline |
| `Action_None` | 265 | 300 | 36 | inferred_complete_timeline |
| `Action_None` | 302 | 305 | 4 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 313 | 449 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 275 | 63 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 297 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 222 | 10 | inferred_complete_timeline |
| `Action_None` | 224 | 246 | 23 | inferred_complete_timeline |
| `Action_None` | 254 | 275 | 22 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 301 | 20 | inferred_complete_timeline |
| `Action_None` | 307 | 316 | 10 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 229 | 17 | inferred_complete_timeline |
| `Action_None` | 257 | 274 | 18 | inferred_complete_timeline |
| `Action_None` | 276 | 288 | 13 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–306
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 188 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 226 | 301 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 303 | 306 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `24`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 42–294
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 217 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 251 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 291 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `29`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 108–235
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 185 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 13 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 188 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 217 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 244 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 272 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 281 | 290 | 10 | inferred_complete_timeline |
| `Action_None` | 361 | 425 | 65 | inferred_complete_timeline |
| `Action_None` | 433 | 444 | 12 | inferred_complete_timeline |
| `Action_None` | 447 | 449 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 6–231
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 14 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 146 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 182 | 31 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `26`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 42–351
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 82 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 186 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 213 | 1 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 36–377
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 147 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 186 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 212 | 1 | inferred_complete_timeline |
| `Action_None` | 213 | 213 | 1 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_None` | 254 | 273 | 20 | inferred_complete_timeline |
| `Action_None` | 282 | 290 | 9 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 348 | 357 | 10 | inferred_complete_timeline |
| `Action_None` | 366 | 377 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `25`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 42–449
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 78 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 188 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 212 | 1 | inferred_complete_timeline |
| `Action_None` | 213 | 213 | 1 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 244 | 19 | inferred_complete_timeline |
| `Action_None` | 254 | 261 | 8 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 289 | 9 | inferred_complete_timeline |
| `Action_None` | 292 | 298 | 7 | inferred_complete_timeline |
| `Action_None` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_None` | 330 | 388 | 59 | inferred_complete_timeline |
| `Action_None` | 391 | 400 | 10 | inferred_complete_timeline |
| `Action_None` | 409 | 413 | 5 | inferred_complete_timeline |
| `Action_None` | 425 | 449 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 212 | 190 | inferred_complete_timeline |
| `Action_None` | 213 | 443 | 231 | inferred_complete_timeline |
| `Action_None` | 446 | 447 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 212 | 159 | inferred_complete_timeline |
| `Action_None` | 213 | 274 | 62 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 304 | 23 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 379 | 449 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 243 | 31 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 12 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 212 | 184 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 182 | 30 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 245 | 20 | inferred_complete_timeline |
| `Action_None` | 254 | 274 | 21 | inferred_complete_timeline |
| `Action_None` | 276 | 300 | 25 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 449 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 297 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 30–267 | 232 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 255–274 | 20 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 259–449 | 131 | 8 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 264–352 | 40 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 279–449 | 85 | 6 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 316–370 | 27 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 326–449 | 104 | 6 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 328–449 | 122 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 336–348 | 13 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 342–449 | 98 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 346–351 | 6 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 349–366 | 15 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 356–360 | 5 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 371–412 | 30 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 372–434 | 50 | 5 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 379–449 | 70 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 387–449 | 58 | 4 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 392–449 | 40 | 7 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 401–447 | 14 | 4 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 402–411 | 10 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 416–449 | 34 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 437–449 | 13 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 439–446 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `29` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 190 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 304: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [213-263] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-300] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-334] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [396-425] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-297] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-443] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-274] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-304] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-449] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-13] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-244] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [281-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-425] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-444] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-146] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-188] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [218-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [226-301] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [303-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-217] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [218-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [226-267] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 213, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [213-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-357] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-377] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [293-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-188] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 213, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [213-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-388] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-400] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-413] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-186] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 213, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [213-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-201] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [213-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-231] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [234-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-376] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-352] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-389] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-446] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-347] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-357] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-376] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-354] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-449] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-398] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-400] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-413] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-447] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-398] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-429] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-446] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-402] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-449] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-411] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>