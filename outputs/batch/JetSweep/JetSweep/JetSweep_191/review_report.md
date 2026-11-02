# Play-Annotation-Generator Annotation Review — JetSweep_191

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_191`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 85
- **Ball Tracks:** 0
- **Action Segments:** 235
- **Validation Warnings:** 334
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 207
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DT1 | defense | `11` | `10` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DT1 | `11` | `10` | 16 | START | 16 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 49 | START | 49 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `3` | `2` | 53 | START | 53 | 117 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 53 | START | 59 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 53 | START | 53 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `19` | 53 | START | 53 | 83 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `22` | `21` | 53 | START | 86 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 53 | START | 53 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 58 | END | 49 | 58 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 64 | START | 64 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `0` | 72 | START | 72 | 81 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–247
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_Toss` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 72 | 232 | 161 | inferred_complete_timeline |
| `Action_None` | 234 | 241 | 8 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 119 | 71 | inferred_complete_timeline |
| `Action_None` | 121 | 202 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_BallCarry` | 72 | 81 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 140 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 260 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 281 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 284 | 304 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 316 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 328 | 330 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 335 | 340 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 149 | 101 | inferred_complete_timeline |
| `Action_None` | 152 | 164 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 325 | 158 | inferred_complete_timeline |
| `Action_None` | 328 | 330 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 83 | 35 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 195 | 97 | inferred_complete_timeline |
| `Action_None` | 197 | 208 | 12 | inferred_complete_timeline |
| `Action_None` | 211 | 222 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 293 | 60 | inferred_complete_timeline |
| `Action_None` | 295 | 305 | 11 | inferred_complete_timeline |
| `Action_None` | 307 | 330 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_LeadBlock` | 53 | 117 | 65 | inferred_complete_timeline |
| `Action_LeadBlock` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_None` | 130 | 177 | 48 | inferred_complete_timeline |
| `Action_None` | 179 | 187 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 83 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_None` | 158 | 195 | 38 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 129 | 71 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 177 | 41 | inferred_complete_timeline |
| `Action_None` | 182 | 224 | 43 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 129 | 44 | inferred_complete_timeline |
| `Action_None` | 130 | 191 | 62 | inferred_complete_timeline |
| `Action_None` | 193 | 254 | 62 | inferred_complete_timeline |
| `Action_None` | 257 | 261 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_None` | 271 | 330 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 106 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 101 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_JetMotion` | 16 | 139 | 124 | inferred_complete_timeline |
| `Action_JetMotion` | 141 | 159 | 19 | inferred_complete_timeline |
| `Action_JetMotion` | 161 | 195 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 93 | 45 | inferred_complete_timeline |
| `Action_None` | 95 | 211 | 117 | inferred_complete_timeline |
| `Action_None` | 213 | 285 | 73 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 328 | 346 | 19 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 93 | 45 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 187 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 99 | 51 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 172 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 144 | 96 | inferred_complete_timeline |
| `Action_None` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_None` | 155 | 202 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 114 | 66 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 202 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–330 | 315 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–177 | 178 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–199 | 120 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 76–359 | 205 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 78–80 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 103–264 | 146 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 106–108 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 140–213 | 74 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 162–359 | 198 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 173–209 | 34 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 183–199 | 17 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 183–193 | 11 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 184–186 | 3 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 194–199 | 6 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 198–221 | 9 | 2 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 203–206 | 4 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 204–251 | 25 | 5 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 219–233 | 8 | 3 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 220–330 | 107 | 4 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 222–359 | 70 | 12 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 230–263 | 8 | 2 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 235–330 | 65 | 7 | Undefined position; Undefined team |
| `51` | `63` | Position_Unknown | Team_Unknown | 241–245 | 5 | 1 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 244–271 | 6 | 2 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 246–304 | 55 | 4 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `55` | `72` | Position_Unknown | Team_Unknown | 267–353 | 76 | 5 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 279–280 | 2 | 1 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 279–335 | 12 | 3 | Undefined position; Undefined team |
| `60` | `81` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 284–286 | 3 | 1 | Undefined position; Undefined team |
| `62` | `84` | Position_Unknown | Team_Unknown | 286–292 | 5 | 2 | Undefined position; Undefined team |
| `63` | `86` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `64` | `88` | Position_Unknown | Team_Unknown | 293–315 | 20 | 2 | Undefined position; Undefined team |
| `65` | `89` | Position_Unknown | Team_Unknown | 294–356 | 16 | 4 | Undefined position; Undefined team |
| `66` | `90` | Position_Unknown | Team_Unknown | 294–324 | 28 | 2 | Undefined position; Undefined team |
| `67` | `92` | Position_Unknown | Team_Unknown | 299–330 | 12 | 3 | Undefined position; Undefined team |
| `68` | `93` | Position_Unknown | Team_Unknown | 299–330 | 28 | 3 | Undefined position; Undefined team |
| `69` | `97` | Position_Unknown | Team_Unknown | 302–359 | 58 | 1 | Undefined position; Undefined team |
| `70` | `99` | Position_Unknown | Team_Unknown | 303–304 | 2 | 1 | Undefined position; Undefined team |
| `71` | `102` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `72` | `103` | Position_Unknown | Team_Unknown | 314–323 | 7 | 2 | Undefined position; Undefined team |
| `73` | `105` | Position_Unknown | Team_Unknown | 314–359 | 39 | 3 | Undefined position; Undefined team |
| `74` | `106` | Position_Unknown | Team_Unknown | 321–324 | 4 | 1 | Undefined position; Undefined team |
| `75` | `107` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `76` | `109` | Position_Unknown | Team_Unknown | 331–359 | 24 | 3 | Undefined position; Undefined team |
| `77` | `110` | Position_Unknown | Team_Unknown | 331–333 | 3 | 1 | Undefined position; Undefined team |
| `78` | `111` | Position_Unknown | Team_Unknown | 331–359 | 24 | 2 | Undefined position; Undefined team |
| `79` | `114` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `80` | `116` | Position_Unknown | Team_Unknown | 336–359 | 23 | 2 | Undefined position; Undefined team |
| `81` | `118` | Position_Unknown | Team_Unknown | 336–343 | 7 | 2 | Undefined position; Undefined team |
| `82` | `121` | Position_Unknown | Team_Unknown | 340–355 | 16 | 1 | Undefined position; Undefined team |
| `83` | `126` | Position_Unknown | Team_Unknown | 349–358 | 10 | 1 | Undefined position; Undefined team |
| `84` | `127` | Position_Unknown | Team_Unknown | 354–358 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 53 != Inferred start 59
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (RG): Annotated start 53 != Inferred start 86
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (12 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 65 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 65 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 130 |
| Missing visible bounding boxes during action | 202 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [49–58], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=59.
- ⚠️ Action 'Action_BallCarry' range [72-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-140] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-260] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [284-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [307-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-324] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [328-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-340] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [53-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-293] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-330] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-202] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-325] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-106] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-93] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-285] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [16-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [141-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [161-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-232] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-241] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-224] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-187] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-114] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-83] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-177] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-330] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-229] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-213] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-209] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-223] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-278] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-330] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-233] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-265] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-347] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-246] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-304] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-293] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-307] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-336] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '64' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-343] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-324] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-359] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-347] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-350] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-341] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-350] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-355] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-358] for track '83' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.

</details>