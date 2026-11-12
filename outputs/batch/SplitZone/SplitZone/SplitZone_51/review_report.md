# Play-Annotation-Generator Annotation Review — SplitZone_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_51`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 14 | START | 17 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 14 | START | 17 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 14 | START | 17 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 14 | START | 17 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 14 | START | 17 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 14 | START | 17 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 14 | START | 17 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `23` | `Group` | 14 | START | 22 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 14 | START | 17 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 14 | START | 17 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 14 | START | 17 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 80 | START | 80 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `12` | 83 | START | 83 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `15` | 83 | START | 83 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 83 | START | 83 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 83 | START | 83 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `4` | 83 | START | 96 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `7` | `7` | 90 | START | 90 | 138 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 95 | END | 80 | 95 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 100 | START | 100 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 107 | START | 107 | 294 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | `22` | `21` | 112 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 17–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 95 | 16 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 17–327
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 106 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 294 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 17–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 240 | 161 | inferred_complete_timeline |
| `Action_None` | 242 | 256 | 15 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 17–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 22–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 79 | 58 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 17–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_SplitBlock` | 90 | 138 | 49 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 17–290
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 82 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 142 | 60 | inferred_complete_timeline |
| `Action_None` | 143 | 290 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 17–319
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 82 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 142 | 60 | inferred_complete_timeline |
| `Action_None` | 145 | 278 | 134 | inferred_complete_timeline |
| `Action_None` | 284 | 297 | 14 | inferred_complete_timeline |
| `Action_None` | 308 | 319 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 17–136
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 80 | 95 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 17–297
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 82 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 142 | 44 | inferred_complete_timeline |
| `Action_None` | 143 | 297 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 17–327
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 82 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 142 | 44 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 276 | 126 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 286 | 290 | 5 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 327 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 17–327
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 115 | 36 | inferred_complete_timeline |
| `Action_None` | 120 | 327 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 171 | 92 | inferred_complete_timeline |
| `Action_None` | 177 | 329 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_None` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 278 | 114 | inferred_complete_timeline |
| `Action_None` | 280 | 290 | 11 | inferred_complete_timeline |
| `Action_None` | 298 | 318 | 21 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 17–121
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 121 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 252 | 173 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 272 | 292 | 21 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 329 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 310 | 231 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 166 | 87 | inferred_complete_timeline |
| `Action_None` | 168 | 284 | 117 | inferred_complete_timeline |
| `Action_None` | 288 | 294 | 7 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 17–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 154 | 75 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 276 | 106 | inferred_complete_timeline |
| `Action_None` | 278 | 329 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 21–73 | 29 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 26–28 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 65–190 | 80 | 7 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 111–329 | 219 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 118–137 | 19 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 130–329 | 194 | 4 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 142–149 | 8 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 161–165 | 5 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 190–194 | 5 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 222–265 | 33 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 276–280 | 5 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 303–304 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 306–308 | 3 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 316–326 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [80–95], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=96.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '21' has invalid range: start=112, end=73. Clamping end to start.
- ⚠️ Action 'Action_None' range [80-171] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-276] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-99] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [90-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-327] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-294] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [296-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [326-327] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-278] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-276] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-252] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-292] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-297] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-123] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-136] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-318] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-49] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-91] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-137] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-218] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-252] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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