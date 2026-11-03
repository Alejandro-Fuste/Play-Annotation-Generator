# Play-Annotation-Generator Annotation Review — Slants0to10_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_95`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 231
- **Validation Warnings:** 251
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 210
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | TE1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | RG | `11` | `11` | 2 | START | 2 | 4 |
| ✅ EXACT | `Action_PassBlock` | RG | `11` | `11` | 5 | START | 5 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 5 | START | 5 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 5 | START | 5 | 61 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 5 | START | 5 | 58 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 5 | START | 5 | 36 |
| ✅ EXACT | `Action_RunSlantRoute` | TE1 | `2` | `2` | 10 | START | 10 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 11 | END | 2 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 52 | START | 52 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE1 | `2` | `2` | 89 | START | 89 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_None` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_ThrowPass` | 52 | 59 | 8 | inferred_complete_timeline |
| `Action_None` | 60 | 193 | 134 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 244 | 40 | inferred_complete_timeline |
| `Action_None` | 253 | 283 | 31 | inferred_complete_timeline |
| `Action_None` | 285 | 329 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 265 | 17 | inferred_complete_timeline |
| `Action_None` | 270 | 274 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 127 | 126 | inferred_complete_timeline |
| `Action_None` | 136 | 166 | 31 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 249 | 48 | inferred_complete_timeline |
| `Action_None` | 256 | 274 | 19 | inferred_complete_timeline |
| `Action_None` | 281 | 308 | 28 | inferred_complete_timeline |
| `Action_None` | 311 | 320 | 10 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 182 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 10 | 79 | 70 | inferred_complete_timeline |
| `Action_None` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 155 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 315 | 142 | inferred_complete_timeline |
| `Action_BallCarry` | 318 | 320 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 14 | 13 | inferred_complete_timeline |
| `Action_None` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 68 | 33 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 171 | 83 | inferred_complete_timeline |
| `Action_None` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 268 | 72 | inferred_complete_timeline |
| `Action_None` | 273 | 288 | 16 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 167 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 193 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 222 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 259 | 274 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 276 | 284 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 293 | 311 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 58 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 111 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 121 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 82 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 36 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 170 | 193 | 24 | inferred_complete_timeline |
| `Action_None` | 196 | 234 | 39 | inferred_complete_timeline |
| `Action_None` | 236 | 306 | 71 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 82 | 81 | inferred_complete_timeline |
| `Action_None` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 101 | 133 | 33 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 81 | 80 | inferred_complete_timeline |
| `Action_None` | 87 | 181 | 95 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 231 | 31 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 299 | 53 | inferred_complete_timeline |
| `Action_None` | 301 | 321 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 178 | 177 | inferred_complete_timeline |
| `Action_None` | 180 | 188 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 220 | 318 | 99 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 133 | 132 | inferred_complete_timeline |
| `Action_None` | 135 | 155 | 21 | inferred_complete_timeline |
| `Action_None` | 157 | 182 | 26 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 254 | 273 | 20 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 323 | 38 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 148 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_None` | 54 | 185 | 132 | inferred_complete_timeline |
| `Action_None` | 201 | 221 | 21 | inferred_complete_timeline |
| `Action_None` | 224 | 247 | 24 | inferred_complete_timeline |
| `Action_None` | 252 | 260 | 9 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 286 | 6 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_None` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_None` | 24 | 311 | 288 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 158 | 157 | inferred_complete_timeline |
| `Action_None` | 204 | 219 | 16 | inferred_complete_timeline |
| `Action_None` | 221 | 310 | 90 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 169 | 168 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 248 | 52 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–249 | 240 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 26–28 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 41–43 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 42–88 | 20 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 78–329 | 208 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 122–241 | 112 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 166–329 | 133 | 9 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 175–240 | 41 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 204–329 | 105 | 6 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 208–300 | 51 | 10 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 210–229 | 16 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 213–258 | 36 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 227–235 | 9 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 256–329 | 66 | 4 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 270–329 | 60 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 274–276 | 3 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 282–329 | 42 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 287–329 | 24 | 3 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 292–329 | 38 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 304–329 | 25 | 2 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 322–325 | 4 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (10 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (5 segments found)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 192 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [2-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-318] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [174-315] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-273] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-323] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-181] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-231] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-299] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-11] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-22] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-311] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-219] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-310] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-185] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-221] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-260] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-249] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-274] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-193] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-248] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-234] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-306] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [224-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [234-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [259-274] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [276-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [293-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [313-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-82] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-133] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-58] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-171] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-288] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-54] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-141] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-329] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-230] for track '26' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-262] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-238] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-277] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-303] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-289] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>