# Play-Annotation-Generator Annotation Review — Counter_209

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_209`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 185
- **Validation Warnings:** 188
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 161
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR4 | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `13` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `20` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 116 | START | 116 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 120 | START | 120 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 120 | START | 132 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 120 | START | 120 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `11` | 120 | START | 120 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR4 | `13` | `12` | 120 | START | 120 | 206 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 131 | END | 116 | 131 |
| ✅ EXACT | `Action_BallCarry` | QB | `18` | `17` | 155 | START | 155 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_None` | 132 | 154 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 224 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 267 | 152 | inferred_complete_timeline |
| `Action_None` | 275 | 381 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 389 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 219 | 104 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 389 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 120 | 206 | 87 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 389 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 215 | 100 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 228 | 235 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 162 | 26 | inferred_complete_timeline |
| `Action_None` | 164 | 215 | 52 | inferred_complete_timeline |
| `Action_None` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 257 | 285 | 29 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_None` | 310 | 352 | 43 | inferred_complete_timeline |
| `Action_None` | 356 | 359 | 4 | inferred_complete_timeline |
| `Action_None` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 150 | 31 | inferred_complete_timeline |
| `Action_PullBlock` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 180 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 182 | 216 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 219 | 235 | 17 | inferred_complete_timeline |
| `Action_None` | 236 | 283 | 48 | inferred_complete_timeline |
| `Action_None` | 285 | 289 | 5 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 318 | 5 | inferred_complete_timeline |
| `Action_None` | 321 | 333 | 13 | inferred_complete_timeline |
| `Action_None` | 338 | 341 | 4 | inferred_complete_timeline |
| `Action_None` | 343 | 389 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 215 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 231 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_DownBlock` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 148 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 162 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_DownBlock` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 235 | 71 | inferred_complete_timeline |
| `Action_None` | 236 | 389 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 148 | 10 | inferred_complete_timeline |
| `Action_None` | 151 | 162 | 12 | inferred_complete_timeline |
| `Action_None` | 164 | 215 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 162 | 47 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_None` | 181 | 215 | 35 | inferred_complete_timeline |
| `Action_None` | 219 | 225 | 7 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 266 | 6 | inferred_complete_timeline |
| `Action_None` | 268 | 389 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 250 | 374 | 125 | inferred_complete_timeline |
| `Action_None` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 242 | 127 | inferred_complete_timeline |
| `Action_None` | 245 | 255 | 11 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 337 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 389 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 265 | 150 | inferred_complete_timeline |
| `Action_None` | 272 | 362 | 91 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 300 | 185 | inferred_complete_timeline |
| `Action_None` | 302 | 389 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 222 | 107 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 253 | 268 | 16 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_None` | 279 | 315 | 37 | inferred_complete_timeline |
| `Action_None` | 317 | 319 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 279 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 179 | 64 | inferred_complete_timeline |
| `Action_None` | 181 | 192 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 215 | 22 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `28` | Position_Unknown | Team_Unknown | 196–389 | 192 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 228–389 | 159 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 230–389 | 158 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 237–290 | 42 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 243–266 | 23 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 246–389 | 142 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 262–302 | 32 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 297–325 | 21 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 311–389 | 77 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 326–389 | 64 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 327–355 | 20 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 330–351 | 18 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 337–338 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 341–389 | 46 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 348–364 | 15 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 355–389 | 29 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 376–383 | 6 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 383–389 | 5 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 143 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (LG) duration 116 frames exceeds threshold 90 frames [start=120, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (RT) duration 116 frames exceeds threshold 90 frames [start=120, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 112 frames exceeds threshold 90 frames [start=120, end=231].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [116–131], lower_priority='Action_DownBlock' annotated_start=120, effective_Action_DownBlock_start=132.
- ⚠️ Action 'Action_None' range [116-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-162] for track '1' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-162] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-215] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-374] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-215] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-162] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-352] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [120-150] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [153-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-283] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-333] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [120-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [208-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-337] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-192] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-362] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-142] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-162] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [165-235] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-381] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [165-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [172-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-215] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-148] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-162] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-310] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-250] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-248] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-262] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-276] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-349] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-389] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-343] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-364] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-370] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '40' has 1 frames without a visible bounding box.
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