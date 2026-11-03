# Play-Annotation-Generator Annotation Review — StopAndGo_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_41`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 197
- **Validation Warnings:** 211
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 4 | START | 4 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 7 | START | 19 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 7 | START | 7 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 7 | START | 7 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 7 | START | 7 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 7 | START | 7 | 246 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 18 | END | 4 | 18 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 18 | START | 18 | 77 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 78 | START | 78 | 94 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `0` | `0` | 95 | START | 95 | 277 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 95 | START | 95 | 105 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_None` | 19 | 94 | 76 | inferred_complete_timeline |
| `Action_ThrowPass` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 299 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 85 | 82 | inferred_complete_timeline |
| `Action_None` | 92 | 231 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 248 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_VerticalStem` | 18 | 77 | 60 | inferred_complete_timeline |
| `Action_SellStop` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 95 | 277 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 64 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 167 | 161 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 179 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 42 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 118 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 37 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 255 | 217 | inferred_complete_timeline |
| `Action_PassBlock` | 262 | 299 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 34 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 107 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 246 | 240 | inferred_complete_timeline |
| `Action_PassBlock` | 251 | 299 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 60 | 57 | inferred_complete_timeline |
| `Action_None` | 70 | 118 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |
| `Action_None` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_None` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 194 | 53 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 249 | 41 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 299 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 44 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 133 | 130 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 169 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 119 | 116 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 177 | 32 | inferred_complete_timeline |
| `Action_None` | 184 | 208 | 25 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 271 | 15 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 214 | 211 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 267 | 20 | inferred_complete_timeline |
| `Action_None` | 269 | 288 | 20 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 185 | 182 | inferred_complete_timeline |
| `Action_None` | 187 | 193 | 7 | inferred_complete_timeline |
| `Action_None` | 197 | 223 | 27 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 264 | 34 | inferred_complete_timeline |
| `Action_None` | 267 | 274 | 8 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 290 | 9 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 76 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 199 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 106 | 103 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 125 | 122 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 59–139 | 77 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 71–81 | 11 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 90–297 | 183 | 7 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 115–120 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 152–299 | 80 | 9 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 156–298 | 59 | 12 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 163–251 | 57 | 6 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 165–232 | 48 | 5 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 179–205 | 16 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 190–295 | 88 | 7 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 190–246 | 48 | 4 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 202–299 | 61 | 6 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 216–299 | 82 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 217–245 | 29 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 218–242 | 19 | 3 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 224–299 | 65 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 226–288 | 63 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 227–230 | 4 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 259–299 | 40 | 2 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 279–299 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 156 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [4–18], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=19.
- ⚠️ Action 'Action_RunGoRoute' range [95-277] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-248] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-199] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-118] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-214] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-44] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-142] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-208] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-271] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-185] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-223] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-134] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-249] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-37] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-255] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-42] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-65] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-167] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-107] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-246] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-128] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-245] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-214] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-244] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-265] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-235] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-275] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-295] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-246] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-299] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-245] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-243] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-266] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-288] for track '39' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-299] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '47' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>