# Play-Annotation-Generator Annotation Review — Counter_261

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_261`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 180
- **Validation Warnings:** 198
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `23` | `Group` | 0 | START | 13 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 90 | START | 90 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 93 | START | 115 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `1` | 93 | START | 93 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `19` | 93 | START | 93 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `13` | `12` | 93 | START | 93 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `3` | `2` | 93 | START | 93 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 105 | END | 90 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 136 | START | 136 | 146 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 197 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 105 | 16 | inferred_complete_timeline |
| `Action_None` | 106 | 135 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 389 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 13–102
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 89 | 77 | inferred_complete_timeline |
| `Action_None` | 90 | 102 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 137 | 48 | inferred_complete_timeline |
| `Action_None` | 162 | 264 | 103 | inferred_complete_timeline |
| `Action_None` | 267 | 311 | 45 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 343 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 281 | 192 | inferred_complete_timeline |
| `Action_None` | 300 | 304 | 5 | inferred_complete_timeline |
| `Action_None` | 307 | 321 | 15 | inferred_complete_timeline |
| `Action_None` | 326 | 344 | 19 | inferred_complete_timeline |
| `Action_None` | 346 | 367 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 165 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 93 | 127 | 35 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 197 | 65 | inferred_complete_timeline |
| `Action_None` | 198 | 372 | 175 | inferred_complete_timeline |
| `Action_None` | 376 | 381 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 105 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 177 | 55 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 250 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 157 | 65 | inferred_complete_timeline |
| `Action_PullBlock` | 159 | 197 | 39 | inferred_complete_timeline |
| `Action_None` | 198 | 212 | 15 | inferred_complete_timeline |
| `Action_None` | 218 | 256 | 39 | inferred_complete_timeline |
| `Action_None` | 258 | 280 | 23 | inferred_complete_timeline |
| `Action_None` | 294 | 372 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 172 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 197 | 21 | inferred_complete_timeline |
| `Action_None` | 198 | 205 | 8 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 311 | 92 | inferred_complete_timeline |
| `Action_None` | 314 | 319 | 6 | inferred_complete_timeline |
| `Action_None` | 321 | 337 | 17 | inferred_complete_timeline |
| `Action_None` | 339 | 347 | 9 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 372 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 134 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 197 | 44 | inferred_complete_timeline |
| `Action_None` | 198 | 223 | 26 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 312 | 9 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 342 | 345 | 4 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 352 | 355 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 166 | 77 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 228 | 10 | inferred_complete_timeline |
| `Action_None` | 230 | 259 | 30 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_None` | 271 | 283 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 9–334
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 89 | 81 | inferred_complete_timeline |
| `Action_None` | 90 | 134 | 45 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 154 | 14 | inferred_complete_timeline |
| `Action_None` | 212 | 233 | 22 | inferred_complete_timeline |
| `Action_None` | 235 | 308 | 74 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 194 | 105 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 301 | 82 | inferred_complete_timeline |
| `Action_None` | 303 | 381 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 219 | 130 | inferred_complete_timeline |
| `Action_None` | 224 | 241 | 18 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 138 | 49 | inferred_complete_timeline |
| `Action_None` | 142 | 220 | 79 | inferred_complete_timeline |
| `Action_None` | 227 | 389 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 297 | 208 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 389 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 129 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 259 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–122 | 123 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 114–132 | 19 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 142–389 | 245 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 199–346 | 148 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 201–259 | 57 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 204–250 | 47 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 212–237 | 26 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 231–311 | 81 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 245–387 | 127 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 252–264 | 12 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 255–389 | 126 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 257–366 | 109 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 273–363 | 88 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 279–372 | 74 | 4 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 290–389 | 71 | 5 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 344–372 | 19 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 360–389 | 30 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 363–364 | 2 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 373–378 | 6 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 373–389 | 17 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 373–376 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 147 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 524: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 105 frames exceeds threshold 90 frames [start=93, end=197].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (LG) duration 105 frames exceeds threshold 90 frames [start=93, end=197].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 105 frames exceeds threshold 90 frames [start=93, end=197].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [90–105], lower_priority='Action_DownBlock' annotated_start=93, effective_Action_DownBlock_start=106.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (RG) duration 105 frames exceeds threshold 90 frames [start=93, end=197].
- ⚠️ Action 'Action_None' range [90-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-264] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-311] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-343] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [93-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-372] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-146] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-281] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-344] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-367] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-381] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-259] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-256] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-372] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [90-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-337] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-347] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-372] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-166] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-259] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-283] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-233] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-343] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-346] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-311] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-320] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-387] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-389] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-308] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-363] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-290] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-313] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-379] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-372] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>