# Play-Annotation-Generator Annotation Review — InsideZoneRead_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_105`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 191
- **Validation Warnings:** 209
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 164
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 4 | START | 4 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 4 | START | 4 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 4 | START | 4 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 4 | START | 4 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 4 | START | 4 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 4 | START | 4 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 46 | START | 46 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 49 | START | 65 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 49 | START | 49 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 49 | START | 49 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 49 | START | 49 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 49 | START | 49 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 62 | END | 46 | 62 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 67 | START | 67 | 82 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 83 | START | 83 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 90 | START | 90 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 243 | 154 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–291
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 89 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 110 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 250 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 282 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 291 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–152
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 112 | 67 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 152 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 140 | 9 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 147 | 102 | inferred_complete_timeline |
| `Action_None` | 150 | 299 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–110
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 48 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 110 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–61
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 48 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 61 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 99 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 119 | 1 | inferred_complete_timeline |
| `Action_None` | 120 | 152 | 33 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 48 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 59 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 100 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_None` | 137 | 155 | 19 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 222 | 40 | inferred_complete_timeline |
| `Action_None` | 227 | 270 | 44 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 48 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 204 | 85 | inferred_complete_timeline |
| `Action_None` | 212 | 230 | 19 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 68 | 93 | 26 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 179 | 17 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 63 | 18 | inferred_complete_timeline |
| `Action_None` | 69 | 93 | 25 | inferred_complete_timeline |
| `Action_None` | 103 | 194 | 92 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–98
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 68 | 84 | 17 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–95
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 92 | 22 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–294
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 138 | 93 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 294 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 93 | 48 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 194 | 70 | inferred_complete_timeline |
| `Action_None` | 199 | 205 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–293
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 190 | 145 | inferred_complete_timeline |
| `Action_None` | 195 | 277 | 83 | inferred_complete_timeline |
| `Action_None` | 279 | 293 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 289 | 244 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 153 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–178
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 167 | 122 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 46 | 253 | 208 | inferred_complete_timeline |
| `Action_None` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 277 | 11 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 85–299 | 176 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 138–299 | 119 | 6 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 138–299 | 119 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 168–277 | 91 | 5 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 172–299 | 128 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 186–299 | 108 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 209–243 | 25 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 215–218 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 219–222 | 4 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 220–299 | 74 | 4 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 225–297 | 42 | 9 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 239–263 | 18 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 253–258 | 6 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 269–292 | 4 | 2 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 279–293 | 15 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 155 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=63.
- ⚠️ Action 'Action_None' range [46-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-129] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-299] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-190] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-277] for track '6' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-84] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-282] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [284-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-291] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-194] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-243] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [46-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-99] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-299] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-289] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-110] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-179] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-92] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-106] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-270] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-204] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-230] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-93] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-194] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-98] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-154] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-221] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-228] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-288] for track '25' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-265] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-221] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-273] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-263] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '47' has 1 frames without a visible bounding box.
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

</details>