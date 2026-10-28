# Play-Annotation-Generator Annotation Review — Draw_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_21`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 1
- **Action Segments:** 199
- **Validation Warnings:** 194
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 174
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `9` | `8` | 61 | START | 61 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `16` | 64 | START | 64 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `18` | 64 | START | 64 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `19` | 64 | START | 64 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `20` | 64 | START | 64 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `7` | 64 | START | 64 | 95 |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | `22` | `21` | 66 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 67 | END | 61 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `22` | `21` | 101 | START | 101 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_None` | 68 | 100 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 144 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 233 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 96 | 36 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 134 | 17 | inferred_complete_timeline |
| `Action_None` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 172 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 96 | 36 | inferred_complete_timeline |
| `Action_None` | 99 | 105 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 276 | 216 | inferred_complete_timeline |
| `Action_None` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_None` | 294 | 298 | 5 | inferred_complete_timeline |
| `Action_None` | 301 | 306 | 6 | inferred_complete_timeline |
| `Action_None` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 202 | 142 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_None` | 221 | 229 | 9 | inferred_complete_timeline |
| `Action_None` | 239 | 252 | 14 | inferred_complete_timeline |
| `Action_None` | 258 | 272 | 15 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 154 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 95 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 146 | 31 | inferred_complete_timeline |
| `Action_None` | 147 | 190 | 44 | inferred_complete_timeline |
| `Action_None` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 89 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 146 | 22 | inferred_complete_timeline |
| `Action_None` | 147 | 298 | 152 | inferred_complete_timeline |
| `Action_None` | 300 | 312 | 13 | inferred_complete_timeline |
| `Action_None` | 314 | 318 | 5 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 96 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 146 | 24 | inferred_complete_timeline |
| `Action_None` | 147 | 275 | 129 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |
| `Action_None` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_None` | 310 | 326 | 17 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 83 | 23 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 123 | 17 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 209 | 149 | inferred_complete_timeline |
| `Action_None` | 239 | 316 | 78 | inferred_complete_timeline |
| `Action_None` | 318 | 325 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 74 | 14 | inferred_complete_timeline |
| `Action_None` | 78 | 95 | 18 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 71 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 180 | 64 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 193 | 329 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 208 | 148 | inferred_complete_timeline |
| `Action_None` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 306 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 109 | 49 | inferred_complete_timeline |
| `Action_None` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_None` | 166 | 185 | 20 | inferred_complete_timeline |
| `Action_None` | 188 | 202 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_None` | 68 | 314 | 247 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 77 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 202 | 142 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 209 | 149 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 237 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 186 | 126 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 238 | 14 | inferred_complete_timeline |
| `Action_None` | 242 | 247 | 6 | inferred_complete_timeline |
| `Action_None` | 249 | 274 | 26 | inferred_complete_timeline |
| `Action_None` | 282 | 291 | 10 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 86–96 | 7 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 106–167 | 62 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 121–329 | 209 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 122–329 | 168 | 12 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 124–245 | 102 | 11 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 138–329 | 176 | 7 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 143–180 | 38 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 172–220 | 36 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 179–329 | 143 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 195–329 | 109 | 7 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 205–329 | 125 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 230–329 | 96 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 273–321 | 47 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 288–292 | 5 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 303–308 | 6 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 319–329 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `32` | `40` | 198 | 198 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (4 segments found)
- ❌ Missing segment for action `Action_FakePassDroptoHandoff` on target `22` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 160 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_FakePassDroptoHandoff' for track '21' has invalid range: start=66, end=60. Clamping end to start.
- ⚠️ Action 'Action_None' range [61-276] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-172] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-208] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-306] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-123] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-95] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-316] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-109] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-53] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-86] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-90] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-116] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-326] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-144] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-233] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-271] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-303] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-166] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-297] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-251] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-321] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '38' has 1 frames without a visible bounding box.
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