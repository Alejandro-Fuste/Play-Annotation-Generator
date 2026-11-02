# Play-Annotation-Generator Annotation Review — JetSweep_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_76`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 42
- **Ball Tracks:** 1
- **Action Segments:** 122
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `9` | `8` | 64 | START | 64 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 102 | START | 102 | 112 |
| ✅ EXACT | `Action_LeadBlock` | RB | `4` | `3` | 103 | START | 103 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `2` | `1` | 103 | START | 103 | 196 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 103 | START | 113 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `13` | 103 | START | 103 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 103 | START | 103 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 103 | START | 103 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 103 | START | 103 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 112 | END | 102 | 112 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 118 | START | 118 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `9` | `8` | 132 | START | 132 | 357 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_Toss` | 118 | 131 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 419 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_LeadBlock` | 103 | 189 | 87 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 419 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 419 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_JetMotion` | 64 | 131 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 357 | 226 | inferred_complete_timeline |
| `Action_BallCarry` | 359 | 388 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 392 | 398 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 403 | 412 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 319 | 218 | inferred_complete_timeline |
| `Action_None` | 321 | 419 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SealBlock` | 103 | 196 | 94 | inferred_complete_timeline |
| `Action_SealBlock` | 199 | 205 | 7 | inferred_complete_timeline |
| `Action_SealBlock` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_SealBlock` | 219 | 225 | 7 | inferred_complete_timeline |
| `Action_SealBlock` | 227 | 419 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 143 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 127 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 172 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 191 | 79 | inferred_complete_timeline |
| `Action_None` | 192 | 321 | 130 | inferred_complete_timeline |
| `Action_None` | 323 | 419 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 191 | 89 | inferred_complete_timeline |
| `Action_None` | 192 | 286 | 95 | inferred_complete_timeline |
| `Action_None` | 290 | 366 | 77 | inferred_complete_timeline |
| `Action_None` | 368 | 419 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 120 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 139 | 38 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 419 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 159 | 58 | inferred_complete_timeline |
| `Action_None` | 161 | 188 | 28 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 137 | 36 | inferred_complete_timeline |
| `Action_None` | 146 | 357 | 212 | inferred_complete_timeline |
| `Action_None` | 360 | 392 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 260 | 159 | inferred_complete_timeline |
| `Action_None` | 266 | 419 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 139 | 38 | inferred_complete_timeline |
| `Action_None` | 141 | 163 | 23 | inferred_complete_timeline |
| `Action_None` | 166 | 419 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 196 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 351 | 250 | inferred_complete_timeline |
| `Action_None` | 354 | 390 | 37 | inferred_complete_timeline |
| `Action_None` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 319 | 218 | inferred_complete_timeline |
| `Action_None` | 321 | 419 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 315 | 214 | inferred_complete_timeline |
| `Action_None` | 317 | 419 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 257 | 156 | inferred_complete_timeline |
| `Action_None` | 260 | 286 | 27 | inferred_complete_timeline |
| `Action_None` | 288 | 419 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 205 | 104 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 237 | 24 | inferred_complete_timeline |
| `Action_None` | 239 | 277 | 39 | inferred_complete_timeline |
| `Action_None` | 280 | 321 | 42 | inferred_complete_timeline |
| `Action_None` | 324 | 419 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 138–419 | 275 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 148–419 | 270 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 192–358 | 167 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 208–419 | 206 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 226–419 | 192 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 318–321 | 4 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 320–322 | 3 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 331–332 | 2 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 336–365 | 9 | 2 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 340–342 | 3 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 352–419 | 46 | 3 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 373–419 | 42 | 2 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 379–412 | 13 | 4 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 399–402 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `33` | `49` | 325 | 337 | 11 | 84.6% | 334–335 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `2` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 103 != Inferred start 113
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [102–112], lower_priority='Action_ZoneBlock' annotated_start=103, effective_Action_ZoneBlock_start=113.
- ⚠️ Action 'Action_None' range [102-319] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [103-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [199-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [207-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [219-225] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [227-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-319] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [103-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-237] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-419] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-315] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-419] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-357] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [359-388] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [392-398] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [403-412] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [418-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-366] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-351] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-357] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-392] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-143] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-419] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-358] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-341] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-362] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-406] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-412] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '42' has 1 frames without a visible bounding box.
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

</details>