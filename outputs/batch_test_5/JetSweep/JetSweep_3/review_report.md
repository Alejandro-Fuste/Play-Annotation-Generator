# TapeVision Annotation Review — JetSweep_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_3`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Toss` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | defense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `4` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 2 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 2 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 2 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `18` | `Group` | 2 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 2 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 2 | START | 0 | 20 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 21 | START | 21 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 40 | START | 40 | 54 |
| ✅ EXACT | `Action_LeadBlock` | TE | `13` | `12` | 41 | START | 41 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 41 | START | 41 | 127 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 41 | START | 56 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 41 | START | 41 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `20` | 41 | START | 41 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 41 | START | 41 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 55 | END | 40 | 55 |
| ✅ EXACT | `Action_Toss` | QB | `20` | `19` | 61 | START | 61 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `5` | `4` | 71 | START | 71 | 247 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | `2` | `1` | 86 | START | 86 | 127 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `15` | `14` | 127 | BOUNDARY | 41 | 127 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `16` | `15` | 127 | BOUNDARY | 56 | 127 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `19` | `18` | 127 | BOUNDARY | 74 | 127 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `21` | `20` | 127 | BOUNDARY | 41 | 127 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `4` | `3` | 127 | BOUNDARY | 41 | 127 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_None` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_Toss` | 61 | 70 | 10 | inferred_complete_timeline |
| `Action_None` | 71 | 229 | 159 | inferred_complete_timeline |
| `Action_None` | 231 | 243 | 13 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 256 | 276 | 21 | inferred_complete_timeline |
| `Action_None` | 278 | 284 | 7 | inferred_complete_timeline |
| `Action_None` | 288 | 298 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 192 | 153 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 282 | 243 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_JetMotion` | 21 | 70 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 247 | 177 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 285 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 119 | 80 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_LeadBlock` | 41 | 127 | 87 | inferred_complete_timeline |
| `Action_None` | 128 | 245 | 118 | inferred_complete_timeline |
| `Action_None` | 247 | 299 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 127 | 87 | inferred_complete_timeline |
| `Action_None` | 128 | 266 | 139 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 127 | 87 | inferred_complete_timeline |
| `Action_None` | 128 | 280 | 153 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 127 | 72 | inferred_complete_timeline |
| `Action_None` | 128 | 227 | 100 | inferred_complete_timeline |
| `Action_None` | 231 | 251 | 21 | inferred_complete_timeline |
| `Action_None` | 253 | 285 | 33 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 127 | 54 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 127 | 87 | inferred_complete_timeline |
| `Action_None` | 128 | 251 | 124 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 89 | 50 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_None` | 64 | 96 | 33 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 86 | 127 | 42 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 292 | 253 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 299 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 74 | 35 | inferred_complete_timeline |
| `Action_None` | 76 | 85 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 96 | 57 | inferred_complete_timeline |
| `Action_None` | 101 | 143 | 43 | inferred_complete_timeline |
| `Action_None` | 148 | 183 | 36 | inferred_complete_timeline |
| `Action_None` | 185 | 299 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 109 | 70 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 275 | 236 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 233 | 194 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 299 | 260 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 92–100 | 9 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 110–299 | 184 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 119–191 | 27 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 190–299 | 98 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 206–299 | 79 | 7 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 220–247 | 5 | 2 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 230–244 | 10 | 3 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 241–245 | 5 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 243–295 | 22 | 3 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 246–299 | 19 | 7 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 251–299 | 24 | 4 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 274–299 | 17 | 5 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 275–298 | 13 | 5 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 282–299 | 11 | 3 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 290–299 | 9 | 2 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 41 != Inferred start 56
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [40–55], lower_priority='Action_ZoneBlock' annotated_start=41, effective_Action_ZoneBlock_start=56.
- ⚠️ Action 'Action_None' range [40-282] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-96] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-247] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-285] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-292] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [297-298] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-299] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-233] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-96] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [41-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-127] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-280] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [40-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-227] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-285] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-192] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-229] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-243] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-276] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-251] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-265] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-233] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-285] for track '29' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '44' has 1 frames without a visible bounding box.
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

</details>