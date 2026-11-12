# Play-Annotation-Generator Annotation Review — SplitZone_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_39`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `27` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `23` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `24` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `25` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `27` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `22` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 6 | START | 6 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 6 | START | 6 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 6 | START | 52 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 6 | START | 55 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 6 | START | 62 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `23` | `Group` | 6 | START | 62 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `24` | `Group` | 6 | START | 62 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `25` | `Group` | 6 | START | 62 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `27` | `Group` | 6 | START | 65 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 6 | START | 6 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 6 | START | 6 | 158 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `16` | 117 | START | 117 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `16` | 120 | START | 132 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `23` | `18` | 120 | START | 120 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `24` | `19` | 120 | START | 120 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `25` | `20` | 120 | START | 120 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `27` | `21` | 120 | START | 120 | 141 |
| ✅ EXACT | `Action_SplitBlock` | TE | `22` | `17` | 124 | START | 124 | 232 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `15` | 128 | END | 117 | 128 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `15` | 142 | START | 142 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 159 | START | 159 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 52–329
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 52 | 116 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 141 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 158 | 17 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–310
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 158 | 153 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 298 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 303 | 310 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–251
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 190 | 74 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 243 | 35 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 62–329
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 123 | 62 | inferred_complete_timeline |
| `Action_SplitBlock` | 124 | 232 | 109 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `25`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 62–246
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 119 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 131 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 232 | 79 | inferred_complete_timeline |
| `Action_None` | 233 | 246 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `27`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `27`
- **team_side:** `offense`
- **Visible Frames:** 65–220
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 65 | 119 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 141 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 220 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 55–329
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 55 | 116 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 144 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 157 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 183 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 232 | 19 | inferred_complete_timeline |
| `Action_None` | 233 | 312 | 80 | inferred_complete_timeline |
| `Action_None` | 319 | 325 | 7 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 62–181
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 119 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 157 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `23`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 62–272
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 119 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 159 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 232 | 72 | inferred_complete_timeline |
| `Action_None` | 233 | 272 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–329
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 46–329
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 100 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 164 | 48 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 275 | 42 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `28`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `28`
- **team_side:** `defense`
- **Visible Frames:** 67–203
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 67 | 116 | 50 | inferred_complete_timeline |
| `Action_None` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 179 | 198 | 20 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 116 | 53 | inferred_complete_timeline |
| `Action_None` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 37–225
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 116 | 60 | inferred_complete_timeline |
| `Action_None` | 117 | 159 | 43 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 215 | 51 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 314 | 198 | inferred_complete_timeline |
| `Action_None` | 316 | 326 | 11 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 308 | 192 | inferred_complete_timeline |
| `Action_None` | 310 | 317 | 8 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 212 | 96 | inferred_complete_timeline |
| `Action_None` | 215 | 303 | 89 | inferred_complete_timeline |
| `Action_None` | 305 | 324 | 20 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 116 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 329 | 213 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 14–24 | 5 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 167–329 | 157 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 184–284 | 26 | 6 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 185–191 | 7 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 206–329 | 105 | 7 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 238–277 | 22 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 253–329 | 75 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 270–329 | 60 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 282–329 | 48 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 288–329 | 39 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 293–314 | 16 | 4 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `23` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `24` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `25` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `27` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [117–128], lower_priority='Action_ZoneBlock' annotated_start=120, effective_Action_ZoneBlock_start=129.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 101 frames exceeds threshold 90 frames [start=120, end=220].
- ⚠️ Action 'Action_None' range [117-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-308] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-317] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-310] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-314] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-24] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-59] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-100] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-164] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [117-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-183] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-159] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-157] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-220] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-329] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-287] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-312] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-304] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>