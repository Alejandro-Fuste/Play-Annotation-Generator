# Play-Annotation-Generator Annotation Review — InsideZoneRead_351

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_351`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 199
- **Validation Warnings:** 189
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 174
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 13 | START | 13 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 16 | START | 29 | 30 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 16 | START | 16 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 16 | START | 16 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 16 | START | 16 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 16 | START | 16 | 36 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 28 | END | 13 | 28 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 33 | START | 33 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `12` | `11` | 44 | START | 44 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 69 | START | 69 | 80 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_None` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_Keep` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_Keep` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 211 | 130 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 133 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 86 | 74 | inferred_complete_timeline |
| `Action_None` | 95 | 114 | 20 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 127 | 147 | 21 | inferred_complete_timeline |
| `Action_None` | 157 | 227 | 71 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 227 | 215 | inferred_complete_timeline |
| `Action_None` | 230 | 244 | 15 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 276 | 16 | inferred_complete_timeline |
| `Action_None` | 281 | 315 | 35 | inferred_complete_timeline |
| `Action_None` | 317 | 322 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 278 | 266 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 100 | 85 | inferred_complete_timeline |
| `Action_None` | 101 | 323 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 85 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 38 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 89 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 127 | 27 | inferred_complete_timeline |
| `Action_None` | 130 | 159 | 30 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 258 | 6 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 279 | 11 | inferred_complete_timeline |
| `Action_None` | 283 | 289 | 7 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 46 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 48 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 104 | 154 | 51 | inferred_complete_timeline |
| `Action_None` | 156 | 173 | 18 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 57 | 45 | inferred_complete_timeline |
| `Action_None` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 112 | 27 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 142 | 25 | inferred_complete_timeline |
| `Action_None` | 144 | 181 | 38 | inferred_complete_timeline |
| `Action_None` | 242 | 248 | 7 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 55 | 43 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 329 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 54 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 116 | 104 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 183 | 53 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 329 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 329 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 92 | 80 | inferred_complete_timeline |
| `Action_None` | 101 | 329 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 329 | 317 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–329 | 326 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–86 | 8 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 85–329 | 223 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 94–329 | 231 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 101–217 | 111 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 107–329 | 138 | 14 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 125–329 | 152 | 15 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 129–329 | 142 | 14 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 133–320 | 177 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 138–230 | 8 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 229–329 | 94 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 247–280 | 29 | 4 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 269–329 | 53 | 3 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 158 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 702: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=29.
- ⚠️ Action 'Action_None' range [13-278] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-227] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-276] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-48] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-147] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-55] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-183] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [44-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-211] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-133] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-323] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-181] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-72] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-49] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-154] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-173] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-38] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-89] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-159] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-279] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-196] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-223] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-316] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-183] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-288] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-263] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '33' has 2 frames without a visible bounding box.
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

</details>