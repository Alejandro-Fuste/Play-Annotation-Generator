# Play-Annotation-Generator Annotation Review — OutRoutes_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_69`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 22 | START | 22 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 22 | START | 22 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 22 | START | 22 | 74 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 22 | START | 22 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 22 | START | 22 | 302 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 28 | END | 28 | 28 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `1` | `1` | 29 | START | 29 | 115 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 78 | START | 78 | 83 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `1` | `1` | 116 | START | 116 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `1` | `1` | 125 | START | 125 | 169 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 77 | 49 | inferred_complete_timeline |
| `Action_ThrowPass` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 256 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 103 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 419 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 188 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunOutRoute` | 29 | 115 | 87 | inferred_complete_timeline |
| `Action_SecureCatch` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 169 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 208 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 236 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 233 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 80 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 74 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 206 | 111 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 215 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 225 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 227 | 307 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 74 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 257 | 164 | inferred_complete_timeline |
| `Action_PassBlock` | 259 | 298 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 301 | 419 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 302 | 281 | inferred_complete_timeline |
| `Action_PassBlock` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 308 | 419 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 163 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 351 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 374 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 383 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 419 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 419 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 91 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 419 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 419 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 300 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 314 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 419 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 143 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 63–66 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 66–419 | 354 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 71–73 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 73–84 | 12 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 107–419 | 308 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 191–280 | 48 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 199–419 | 159 | 4 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 210–245 | 17 | 5 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 236–272 | 37 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 243–394 | 141 | 4 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 253–419 | 167 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 253–419 | 147 | 4 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 263–276 | 6 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 283–419 | 137 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 285–419 | 134 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 326–419 | 94 | 1 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 339–391 | 47 | 3 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 372–411 | 16 | 3 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 412–418 | 7 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 102 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [125-169] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-101] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-188] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-419] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-418] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-419] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [304-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [308-419] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-163] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-351] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-374] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-383] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-103] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-74] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-87] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-206] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [218-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [227-307] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [259-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-233] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-419] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-232] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-377] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-272] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-281] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-381] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-394] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-275] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-315] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-419] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-419] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-316] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-366] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-386] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-391] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-380] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-394] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-411] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-418] for track '44' has 2 frames without a visible bounding box.
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