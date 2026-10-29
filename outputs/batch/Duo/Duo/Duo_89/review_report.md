# Play-Annotation-Generator Annotation Review — Duo_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_89`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 358
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 218
- **Validation Warnings:** 247
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LB2 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | DE2 | defense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | LB2 | defense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_ComboBlock` | LB2 | `11` | `11` | 152 | START | 152 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `12` | `12` | 152 | START | 152 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | DE2 | `15` | `15` | 152 | START | 152 | 169 |
| ✅ EXACT | `Action_ComboBlock` | LT | `9` | `9` | 152 | START | 152 | 208 |
| ✅ EXACT | `Action_BlockSecondLevel` | LB2 | `11` | `11` | 184 | START | 184 | 208 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 117 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 248 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 261 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 314 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 322 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 251 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 282 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 308 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 351 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 358 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 192 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 185 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 244 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 208 | 57 | inferred_complete_timeline |
| `Action_None` | 209 | 260 | 52 | inferred_complete_timeline |
| `Action_None` | 276 | 289 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 179 | 28 | inferred_complete_timeline |
| `Action_ComboBlock` | 184 | 208 | 25 | inferred_complete_timeline |
| `Action_None` | 209 | 241 | 33 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 37 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 142 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 198 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 238 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 265 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 294 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 348 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 89 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 187 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 241 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 358 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 113 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 169 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 315 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 325 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 151 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 169 | 18 | inferred_complete_timeline |
| `Action_ComboBlock` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_ComboBlock` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 190 | 193 | 4 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 205 | 11 | inferred_complete_timeline |
| `Action_None` | 209 | 237 | 29 | inferred_complete_timeline |
| `Action_None` | 280 | 358 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 113 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 190 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 249 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 247 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 145 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 152 | 183 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 184 | 208 | 25 | inferred_complete_timeline |
| `Action_None` | 209 | 236 | 28 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 337 | 6 | inferred_complete_timeline |
| `Action_None` | 340 | 345 | 6 | inferred_complete_timeline |
| `Action_None` | 351 | 358 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 246 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 183 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 197 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 238 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 246 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 358 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–351 | 352 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–256 | 234 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 79–358 | 208 | 9 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 165–171 | 7 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 204–238 | 27 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 223–253 | 15 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 226–271 | 30 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 254–358 | 98 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 267–358 | 92 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 271–358 | 88 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 277–358 | 74 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 289–358 | 61 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 294–358 | 58 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 304–340 | 36 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 304–358 | 54 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 306–327 | 22 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 310–354 | 45 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 312–358 | 47 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 340–356 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 204 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 179: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 180: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-113] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-315] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-325] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-129] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-221] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-256] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-247] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-358] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-145] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-337] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-345] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [152-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-282] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-308] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-114] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [152-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [176-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [181-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [190-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [195-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-358] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-244] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-89] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-117] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-142] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-248] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-280] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-314] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-37] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-142] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-265] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-348] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-113] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-89] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-142] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-187] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-241] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-145] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-198] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-259] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-284] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-358] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-358] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-358] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-312] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-358] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-340] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-311] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-358] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-327] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-354] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-358] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-356] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>