# Play-Annotation-Generator Annotation Review — DeepCross_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_3`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 187
- **Validation Warnings:** 234
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 170
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | RG | `19` | `19` | 21 | START | 21 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 24 | START | 24 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 24 | START | 24 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 24 | START | 24 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 24 | START | 24 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `3` | `3` | 34 | START | 34 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 34 | END | 21 | 34 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `15` | `15` | 175 | START | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `27` | `25` | 249 | START | 249 | 250 |

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
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 138 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_None` | 65 | 133 | 69 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 172 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 208 | 188 | inferred_complete_timeline |
| `Action_None` | 212 | 293 | 82 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 108 | 88 | inferred_complete_timeline |
| `Action_None` | 111 | 252 | 142 | inferred_complete_timeline |
| `Action_None` | 292 | 313 | 22 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 136 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 56 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 133 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 136 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 197 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 211 | 220 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 66 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 74 | 54 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 64 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 66 | 46 | inferred_complete_timeline |
| `Action_None` | 77 | 136 | 60 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 255 | 94 | inferred_complete_timeline |
| `Action_None` | 261 | 263 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 349 | 53 | inferred_complete_timeline |
| `Action_None` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 106 | 86 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 359 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 359 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 126 | 106 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 224 | 83 | inferred_complete_timeline |
| `Action_None` | 231 | 241 | 11 | inferred_complete_timeline |
| `Action_None` | 246 | 251 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 177 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 119 | 99 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 209 | 71 | inferred_complete_timeline |
| `Action_None` | 215 | 243 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 167 | 93 | inferred_complete_timeline |
| `Action_None` | 171 | 247 | 77 | inferred_complete_timeline |
| `Action_None` | 251 | 265 | 15 | inferred_complete_timeline |
| `Action_None` | 267 | 287 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 325 | 305 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–124 | 100 | 6 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–359 | 339 | 7 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–275 | 224 | 11 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 89–125 | 33 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 114–133 | 20 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 125–250 | 126 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 128–249 | 115 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 133–184 | 38 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 146–237 | 81 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 159–201 | 42 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 170–183 | 14 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 177–185 | 9 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 202–331 | 130 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 208–269 | 58 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 241–263 | 16 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 259–359 | 99 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 259–359 | 101 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 261–359 | 99 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 264–271 | 7 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 264–351 | 88 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 266–276 | 11 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 269–315 | 28 | 4 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 276–359 | 84 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 287–325 | 39 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 291–323 | 19 | 5 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 294–358 | 47 | 6 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 298–359 | 58 | 3 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 301–303 | 3 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 308–326 | 7 | 2 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 331–359 | 29 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 340–359 | 15 | 3 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 341–359 | 19 | 1 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (10 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `15` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 152 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 6: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '15' has invalid range: start=175, end=138. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-108] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-313] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-66] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-124] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-208] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-293] for track '2' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [34-83] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [95-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-64] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-74] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-66] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-328] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-224] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-359] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-56] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-80] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-133] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-177] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-243] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-66] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-255] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-349] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-66] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-93] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-108] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-66] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-136] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-136] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-197] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [199-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [211-220] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [224-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-107] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-214] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-247] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-198] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-331] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-253] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-253] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-322] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-351] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-276] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-292] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-325] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-322] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-343] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-339] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-359] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>