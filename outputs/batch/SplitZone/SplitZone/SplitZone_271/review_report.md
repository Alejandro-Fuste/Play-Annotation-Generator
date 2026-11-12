# Play-Annotation-Generator Annotation Review — SplitZone_271

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_271`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 169
- **Validation Warnings:** 197
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 145
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 16 | START | 16 | 30 |
| ✅ EXACT | `Action_SplitBlock` | TE | `11` | `11` | 20 | START | 20 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 28 | START | 31 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 28 | START | 28 | 33 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 28 | START | 28 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 28 | START | 28 | 43 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 28 | START | 28 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | QB | `18` | `18` | 29 | START | 31 | 46 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 30 | END | 16 | 30 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `13` | `13` | 35 | START | 35 | 46 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 47 | START | 47 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `13` | 53 | START | 53 | 77 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `16` | `16` | 62 | START | 62 | 83 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_PressEdge` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_PressEdge` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_None` | 65 | 193 | 129 | inferred_complete_timeline |
| `Action_None` | 199 | 287 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_None` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 53 | 77 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 156 | 251 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 285 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 308 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 318 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 39 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 230 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 212 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SplitBlock` | 20 | 62 | 43 | inferred_complete_timeline |
| `Action_None` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 124 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 284 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 69 | 42 | inferred_complete_timeline |
| `Action_None` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_None` | 102 | 162 | 61 | inferred_complete_timeline |
| `Action_None` | 168 | 251 | 84 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 61 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 62 | 83 | 22 | inferred_complete_timeline |
| `Action_None` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 329 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 71 | 21 | inferred_complete_timeline |
| `Action_None` | 99 | 275 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 43 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_None` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_None` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_None` | 129 | 154 | 26 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 230 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 55 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 154 | 139 | inferred_complete_timeline |
| `Action_None` | 172 | 212 | 41 | inferred_complete_timeline |
| `Action_None` | 214 | 252 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 63 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_None` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_None` | 108 | 281 | 174 | inferred_complete_timeline |
| `Action_None` | 284 | 286 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_None` | 63 | 267 | 205 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 281 | 9 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 74 | 59 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 260 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 169 | 154 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 184 | 329 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 93 | 78 | inferred_complete_timeline |
| `Action_None` | 95 | 121 | 27 | inferred_complete_timeline |
| `Action_None` | 123 | 308 | 186 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 110 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 34–76 | 32 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 48–225 | 176 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 95–191 | 84 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 97–130 | 31 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 101–329 | 228 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 106–112 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 121–170 | 46 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 123–128 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 134–230 | 92 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 139–141 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 142–189 | 38 | 4 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 146–160 | 15 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 147–170 | 12 | 3 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 151–179 | 13 | 4 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 171–187 | 15 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 206–269 | 41 | 8 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 247–329 | 79 | 3 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 249–255 | 7 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 249–253 | 5 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 309–329 | 20 | 2 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (12 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 129 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [16-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-39] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-281] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-162] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-93] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-308] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [20-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-284] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [53-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-123] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-285] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [297-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-308] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-267] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-49] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-275] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-260] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-329] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-230] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-163] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-162] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-179] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-160] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-284] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '54' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.

</details>