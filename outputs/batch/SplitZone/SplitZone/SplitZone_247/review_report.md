# Play-Annotation-Generator Annotation Review — SplitZone_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_247`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `0` | `Group` | 10 | START | 12 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 10 | START | 12 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 10 | START | 12 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 10 | START | 12 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 10 | START | 12 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 10 | START | 12 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 10 | START | 12 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 10 | START | 12 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 10 | START | 21 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 10 | START | 12 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 95 | START | 95 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 98 | START | 98 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 98 | START | 98 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 98 | START | 114 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `22` | 98 | START | 98 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `0` | `0` | 102 | START | 102 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 110 | END | 95 | 110 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 117 | START | 117 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `18` | `18` | 121 | START | 126 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE | `15` | `15` | 138 | START | 138 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 12–182
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 157 | 37 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 22 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 50 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 117 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 238 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 101 | 90 | inferred_complete_timeline |
| `Action_SplitBlock` | 102 | 140 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 142 | 174 | 33 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 180 | 86 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 175 | 81 | inferred_complete_timeline |
| `Action_None` | 180 | 204 | 25 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 222 | 7 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 12–270
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 110 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 138 | 158 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_None` | 185 | 228 | 44 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 240 | 247 | 8 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 263 | 7 | inferred_complete_timeline |
| `Action_None` | 265 | 270 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 97 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 138 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 184 | 45 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 21–288
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 67 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 97 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 119 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 184 | 51 | inferred_complete_timeline |
| `Action_None` | 185 | 207 | 23 | inferred_complete_timeline |
| `Action_None` | 211 | 261 | 51 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–158
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 95 | 108 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 158 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–243
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 97 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 138 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 201 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 239 | 30 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–248
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 192 | 98 | inferred_complete_timeline |
| `Action_None` | 194 | 248 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 14–126
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 94 | 81 | inferred_complete_timeline |
| `Action_None` | 95 | 126 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 32 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 94 | 57 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 173 | 79 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 248 | 54 | inferred_complete_timeline |
| `Action_None` | 251 | 284 | 34 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 215 | 121 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–199
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 155 | 61 | inferred_complete_timeline |
| `Action_None` | 194 | 199 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 209 | 115 | inferred_complete_timeline |
| `Action_None` | 215 | 283 | 69 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–248
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 240 | 146 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 12–258 | 247 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 12–18 | 7 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 142–178 | 37 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 167–299 | 126 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 172–196 | 25 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 188–262 | 41 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 192–299 | 108 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 244–299 | 54 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 252–299 | 41 | 3 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 276–299 | 23 | 2 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 286–292 | 7 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 496: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [95–110], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=111.
- ⚠️ Action 'Action_SplitBlock' range [102-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [142-174] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-248] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-215] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-258] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-284] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [138-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-228] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-138] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-22] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-50] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-71] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-238] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [95-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-158] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-94] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-119] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-184] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-261] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-178] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-249] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>