# Play-Annotation-Generator Annotation Review — Draw_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_25`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 175
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 52 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 53 | START | 53 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `10` | 56 | START | 71 | 143 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `15` | 56 | START | 56 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `18` | 56 | START | 56 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `20` | 56 | START | 56 | 83 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `6` | 56 | START | 56 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 70 | END | 53 | 70 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `22` | `21` | 72 | START | 72 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `22` | `21` | 100 | START | 100 | 109 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_None` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 72 | 99 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 142 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 408 | 356 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 304 | 252 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 344 | 21 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_None` | 387 | 395 | 9 | inferred_complete_timeline |
| `Action_None` | 398 | 449 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 335 | 283 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 349 | 5 | inferred_complete_timeline |
| `Action_None` | 353 | 369 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 355 | 303 | inferred_complete_timeline |
| `Action_None` | 358 | 361 | 4 | inferred_complete_timeline |
| `Action_None` | 366 | 370 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 140 | 85 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 291 | 115 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 337 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 140 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BallSnap` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 143 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 153 | 1 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 164 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 178 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 83 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 150 | 66 | inferred_complete_timeline |
| `Action_None` | 154 | 200 | 47 | inferred_complete_timeline |
| `Action_None` | 203 | 229 | 27 | inferred_complete_timeline |
| `Action_None` | 234 | 246 | 13 | inferred_complete_timeline |
| `Action_None` | 248 | 297 | 50 | inferred_complete_timeline |
| `Action_None` | 299 | 344 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 144 | 92 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 173 | 11 | inferred_complete_timeline |
| `Action_None` | 176 | 185 | 10 | inferred_complete_timeline |
| `Action_None` | 187 | 260 | 74 | inferred_complete_timeline |
| `Action_None` | 268 | 283 | 16 | inferred_complete_timeline |
| `Action_None` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_None` | 303 | 355 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 449 | 397 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 133 | 81 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_None` | 157 | 186 | 30 | inferred_complete_timeline |
| `Action_None` | 190 | 218 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 138 | 86 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 186 | 134 | inferred_complete_timeline |
| `Action_None` | 192 | 449 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 144 | 92 | inferred_complete_timeline |
| `Action_None` | 151 | 156 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 449 | 397 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 183 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 291 | 239 | inferred_complete_timeline |
| `Action_None` | 293 | 359 | 67 | inferred_complete_timeline |
| `Action_None` | 363 | 449 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 147 | 95 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 285 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 174 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–76 | 77 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 101–315 | 174 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 108–449 | 335 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 151–369 | 204 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 178–333 | 147 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 191–373 | 161 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 191–252 | 62 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 198–254 | 31 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 201–449 | 215 | 4 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 205–234 | 30 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 219–240 | 8 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 226–449 | 220 | 5 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 244–362 | 119 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 257–449 | 167 | 6 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 259–367 | 74 | 4 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 284–290 | 7 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 294–371 | 61 | 7 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 412–449 | 38 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 445–449 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 123 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [53–70], lower_priority='Action_PassBlock' annotated_start=56, effective_Action_PassBlock_start=71.
- ⚠️ Action 'Action_None' range [53-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-283] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-133] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-408] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-369] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-291] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-337] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-355] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-285] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-344] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-395] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-449] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-291] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-359] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-142] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-297] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-344] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-185] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-186] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-329] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-346] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-373] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-274] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-406] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-234] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-283] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-362] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-265] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-293] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-315] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-318] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-314] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-340] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '44' has 1 frames without a visible bounding box.
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

</details>