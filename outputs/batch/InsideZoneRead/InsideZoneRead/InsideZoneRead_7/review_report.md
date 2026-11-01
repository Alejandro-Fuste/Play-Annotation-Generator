# Play-Annotation-Generator Annotation Review — InsideZoneRead_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_7`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 205
- **Validation Warnings:** 232
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 181
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 28 | START | 28 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 30 | START | 30 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 30 | START | 30 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 30 | START | 30 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 30 | START | 30 | 58 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `8` | 30 | START | 62 | 71 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 42 | END | 28 | 42 |
| ✅ EXACT | `Action_ReadDefender` | QB | `15` | `14` | 46 | START | 46 | 53 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 54 | START | 54 | 64 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `22` | `21` | 65 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_None` | 65 | 244 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 284 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 245 | 218 | inferred_complete_timeline |
| `Action_None` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 119 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 172 | 145 | inferred_complete_timeline |
| `Action_None` | 176 | 202 | 27 | inferred_complete_timeline |
| `Action_None` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_None` | 225 | 232 | 8 | inferred_complete_timeline |
| `Action_None` | 243 | 260 | 18 | inferred_complete_timeline |
| `Action_None` | 262 | 270 | 9 | inferred_complete_timeline |
| `Action_None` | 272 | 284 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 48 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 99 | 40 | inferred_complete_timeline |
| `Action_None` | 100 | 166 | 67 | inferred_complete_timeline |
| `Action_None` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_None` | 240 | 281 | 42 | inferred_complete_timeline |
| `Action_None` | 285 | 295 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 71 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 58 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 73 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 55 | 28 | inferred_complete_timeline |
| `Action_None` | 60 | 158 | 99 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 58 | 31 | inferred_complete_timeline |
| `Action_None` | 60 | 177 | 118 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 227 | 12 | inferred_complete_timeline |
| `Action_None` | 232 | 251 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 43 | 16 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 45 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 47 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 71 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 299 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 214 | 187 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 203 | 176 | inferred_complete_timeline |
| `Action_None` | 205 | 224 | 20 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 101 | 74 | inferred_complete_timeline |
| `Action_None` | 111 | 123 | 13 | inferred_complete_timeline |
| `Action_None` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 211 | 42 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 96 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 21–227 | 172 | 12 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 63–299 | 160 | 13 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 64–75 | 12 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 81–122 | 41 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 93–129 | 37 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 111–299 | 72 | 9 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 121–165 | 26 | 6 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 122–299 | 172 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 123–250 | 24 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 133–299 | 141 | 10 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 136–299 | 164 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 139–150 | 12 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 143–286 | 106 | 6 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 148–222 | 20 | 5 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 178–189 | 5 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 200–299 | 100 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 210–266 | 28 | 6 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 223–291 | 56 | 4 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 246–252 | 7 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 250–259 | 6 | 2 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 263–298 | 15 | 3 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 280–295 | 14 | 3 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 280–299 | 11 | 2 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 281–293 | 9 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 30 != Inferred start 62
- ❌ Missing segment for action `Action_BallCarry` on target `22` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 173 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [28–42], lower_priority='Action_ZoneBlock' annotated_start=30, effective_Action_ZoneBlock_start=43.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=65, end=47. Clamping end to start.
- ⚠️ Action 'Action_None' range [28-119] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-177] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-251] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-55] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-158] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-214] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-101] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-211] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [28-42] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-71] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-260] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-203] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-71] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-244] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-71] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-99] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-166] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-281] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-295] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-45] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-47] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-67] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-58] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-170] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-157] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-129] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-294] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-214] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-288] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-153] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-299] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-286] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-299] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-291] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '49' has 1 frames without a visible bounding box.
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

</details>