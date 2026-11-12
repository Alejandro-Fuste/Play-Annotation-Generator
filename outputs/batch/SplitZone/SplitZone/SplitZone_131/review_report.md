# Play-Annotation-Generator Annotation Review — SplitZone_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_131`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 177
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
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `24` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 26 | START | 27 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 26 | START | 27 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 26 | START | 27 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 26 | START | 27 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 26 | START | 27 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 26 | START | 84 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 26 | START | 85 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 26 | START | 85 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 26 | START | 27 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 26 | START | 27 | 212 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 178 | START | 178 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 181 | START | 191 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 181 | START | 187 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `23` | `22` | 181 | START | 181 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `24` | `23` | 181 | START | 186 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `12` | `12` | 189 | START | 189 | 199 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 190 | END | 178 | 190 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 194 | START | 194 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 213 | START | 213 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 348 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 27–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_SnapReceive` | 178 | 190 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 194 | 209 | 16 | inferred_complete_timeline |
| `Action_None` | 215 | 359 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 212 | 186 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 243 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 270 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 293 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 359 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 291 | 114 | inferred_complete_timeline |
| `Action_None` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 359 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 27–233
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 114 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 188 | 54 | inferred_complete_timeline |
| `Action_SplitBlock` | 189 | 199 | 11 | inferred_complete_timeline |
| `Action_SplitBlock` | 207 | 233 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 85–359
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 270 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 273 | 290 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 348 | 52 | inferred_complete_timeline |
| `Action_None` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 27–290
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 177 | 129 | inferred_complete_timeline |
| `Action_BallSnap` | 178 | 190 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 202 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 269 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 273 | 290 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 85–270
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 180 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 191 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 270 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 84–359
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 273 | 278 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 280 | 285 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 328 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 348 | 18 | inferred_complete_timeline |
| `Action_None` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 27–267
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 69 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 175 | 22 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 198 | 13 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_None` | 225 | 267 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `26`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 148–193
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 270 | 93 | inferred_complete_timeline |
| `Action_None` | 273 | 290 | 18 | inferred_complete_timeline |
| `Action_None` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 359 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 223 | 46 | inferred_complete_timeline |
| `Action_None` | 227 | 244 | 18 | inferred_complete_timeline |
| `Action_None` | 248 | 254 | 7 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 303 | 31 | inferred_complete_timeline |
| `Action_None` | 305 | 338 | 34 | inferred_complete_timeline |
| `Action_None` | 341 | 359 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 359 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 27–290
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 270 | 93 | inferred_complete_timeline |
| `Action_None` | 273 | 290 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 270 | 93 | inferred_complete_timeline |
| `Action_None` | 273 | 285 | 13 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 341 | 10 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_None` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 177 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 290 | 113 | inferred_complete_timeline |
| `Action_None` | 306 | 359 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 27–166 | 132 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 48–86 | 33 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 73–111 | 15 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 79–86 | 7 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 81–87 | 7 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 81–90 | 10 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 190–359 | 94 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 214–359 | 123 | 10 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 216–355 | 131 | 4 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 216–242 | 5 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 242–359 | 99 | 7 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 251–359 | 99 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 298–359 | 61 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 302–359 | 57 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 306–359 | 44 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 307–359 | 53 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 312–317 | 4 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 328–334 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `23` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `24` (6 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 136 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 110 frames exceeds threshold 90 frames [start=181, end=290].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [178–190], lower_priority='Action_ZoneBlock' annotated_start=181, effective_Action_ZoneBlock_start=191.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 168 frames exceeds threshold 90 frames [start=181, end=348].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '23' (LG) duration 168 frames exceeds threshold 90 frames [start=181, end=348].
- ⚠️ Action 'Action_None' range [178-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-303] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-338] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-359] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-270] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-293] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-270] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-359] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-69] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-267] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [189-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [207-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [194-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [273-290] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [273-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [280-285] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [298-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [305-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-180] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-191] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-162] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [226-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [273-290] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-288] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-277] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-335] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-313] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-355] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-341] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>