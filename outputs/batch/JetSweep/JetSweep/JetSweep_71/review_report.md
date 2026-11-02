# Play-Annotation-Generator Annotation Review — JetSweep_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_71`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 178
- **Validation Warnings:** 231
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 147
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `17` | `16` | 70 | START | 70 | 111 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `15` | `14` | 97 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 101 | START | 101 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 101 | START | 101 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 101 | START | 101 | 108 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `15` | `14` | 101 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 101 | START | 101 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 110 | END | 97 | 110 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 116 | START | 116 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 126 | START | 126 | 141 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `19` | `18` | 178 | START | 179 | 212 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_SnapReceive` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_Toss` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_None` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_None` | 158 | 193 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 131 | 35 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 116 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 146 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 147 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 173 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 212 | 12 | inferred_complete_timeline |
| `Action_None` | 213 | 236 | 24 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 199 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 263 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 50 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 18 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 100 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 100 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 133 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 160 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 212 | 49 | inferred_complete_timeline |
| `Action_None` | 213 | 300 | 88 | inferred_complete_timeline |
| `Action_None` | 302 | 312 | 11 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 181 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_None` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 114 | 222 | 109 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 241 | 9 | inferred_complete_timeline |
| `Action_None` | 251 | 276 | 26 | inferred_complete_timeline |
| `Action_None` | 288 | 313 | 26 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 38 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 163 | 67 | inferred_complete_timeline |
| `Action_None` | 190 | 203 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 189 | 93 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 158 | 62 | inferred_complete_timeline |
| `Action_None` | 161 | 186 | 26 | inferred_complete_timeline |
| `Action_None` | 188 | 242 | 55 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 329 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 329 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 195 | 99 | inferred_complete_timeline |
| `Action_None` | 198 | 257 | 60 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–291 | 292 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 70–183 | 101 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 97–164 | 62 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 102–329 | 186 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 169–205 | 37 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 174–236 | 63 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 176–329 | 95 | 9 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 190–327 | 101 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 190–276 | 82 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 191–299 | 108 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 196–201 | 6 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 200–329 | 109 | 5 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 204–236 | 14 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 210–269 | 55 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 212–329 | 118 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 214–291 | 42 | 8 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 227–329 | 92 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 234–243 | 10 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 237–329 | 77 | 3 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 243–256 | 14 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 257–274 | 18 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 278–284 | 4 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 282–329 | 45 | 2 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 288–329 | 42 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 292–329 | 38 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 294–328 | 25 | 4 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 298–329 | 32 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 298–306 | 9 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 299–327 | 28 | 2 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (3 segments found)
- ❌ Missing segment for action `Action_BallSnap` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (11 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (12 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (5 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `19` (Position_Unknown): Annotated start 178 != Inferred start 179

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 152 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 144: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 112 frames exceeds threshold 90 frames [start=101, end=212].
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=97, end=50. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=101, end=50. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-222] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-276] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-313] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-181] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [116-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-257] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-291] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-242] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-173] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-236] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-56] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-160] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-38] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [70-111] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [113-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [120-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-141] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [179-212] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-215] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-225] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-281] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-327] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-276] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-291] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-262] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-263] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-327] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-329] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-306] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-327] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>