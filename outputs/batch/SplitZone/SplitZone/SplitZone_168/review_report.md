# Play-Annotation-Generator Annotation Review — SplitZone_168

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_168`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 179
- **Validation Warnings:** 229
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 135
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `10` | `Group` | 12 | START | 13 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 12 | START | 13 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 12 | START | 13 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 12 | START | 13 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 12 | START | 13 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 12 | START | 13 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 12 | START | 13 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `13` | `13` | 150 | START | 150 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 153 | START | 153 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `12` | 153 | START | 153 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 153 | START | 186 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 153 | START | 153 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 153 | START | 153 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `10` | `10` | 158 | START | 164 | 167 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `9` | `9` | 162 | END | 150 | 162 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `9` | `9` | 170 | START | 170 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 180 | START | 180 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `12` | `12` | 182 | START | 194 | 206 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 228 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–190
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 175 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 153 | 24 | inferred_complete_timeline |
| `Action_SplitBlock` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 169 | 228 | 60 | inferred_complete_timeline |
| `Action_None` | 229 | 359 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–253
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 152 | 140 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 190 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 227 | 21 | inferred_complete_timeline |
| `Action_None` | 239 | 246 | 8 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–219
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 51 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–205
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 30 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 149 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–171
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 51 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 152 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 171 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 50 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 228 | 35 | inferred_complete_timeline |
| `Action_None` | 229 | 359 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–193
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 115 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 149 | 20 | inferred_complete_timeline |
| `Action_None` | 150 | 178 | 29 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–190
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 111 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 149 | 18 | inferred_complete_timeline |
| `Action_None` | 150 | 167 | 18 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 68–297
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 140 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 275 | 14 | inferred_complete_timeline |
| `Action_None` | 280 | 297 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–281
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 149 | 137 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 200 | 26 | inferred_complete_timeline |
| `Action_None` | 203 | 214 | 12 | inferred_complete_timeline |
| `Action_None` | 225 | 231 | 7 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 251 | 10 | inferred_complete_timeline |
| `Action_None` | 254 | 259 | 6 | inferred_complete_timeline |
| `Action_None` | 261 | 271 | 11 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–160
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 149 | 83 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–190
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 149 | 137 | inferred_complete_timeline |
| `Action_None` | 150 | 164 | 15 | inferred_complete_timeline |
| `Action_None` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 181 | 190 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–354
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 149 | 137 | inferred_complete_timeline |
| `Action_None` | 150 | 170 | 21 | inferred_complete_timeline |
| `Action_None` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_None` | 235 | 259 | 25 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 340 | 67 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 354 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 13–352 | 297 | 11 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 191–217 | 4 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 207–359 | 138 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 211–359 | 139 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 213–295 | 74 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 225–239 | 6 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 228–294 | 38 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 228–293 | 12 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 229–359 | 67 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 252–345 | 72 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 256–257 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 258–359 | 100 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 260–290 | 31 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 260–359 | 100 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 260–349 | 90 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 262–359 | 98 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 263–352 | 83 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 268–340 | 73 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 287–359 | 73 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 291–359 | 69 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 304–359 | 56 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 325–352 | 27 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 326–333 | 6 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 172 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 338: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [150–162], lower_priority='Action_ZoneBlock' annotated_start=153, effective_Action_ZoneBlock_start=163.
- ⚠️ Action 'Action_PreSnap' range [13-149] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-170] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-340] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-227] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-152] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '8' starts at frame 180, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [180-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 163, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [163-165] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [170-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-327] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-49] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-108] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [164-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-359] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-152] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '12' starts at frame 153, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [153-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [194-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [218-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-46] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-79] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-87] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-147] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [150-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [158-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-275] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-297] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-297] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-359] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-313] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-359] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-345] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-290] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-349] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-343] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-352] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-333] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>