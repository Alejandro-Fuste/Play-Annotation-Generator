# Play-Annotation-Generator Annotation Review — RPO_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_43`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 80
- **Ball Tracks:** 0
- **Action Segments:** 266
- **Validation Warnings:** 344
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunOutRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 247
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `17` | 46 | START | 46 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 68 | START | 68 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 68 | START | 68 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 68 | START | 68 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 68 | START | 68 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `21` | 68 | START | 68 | 80 |
| ✅ EXACT | `Action_PullBall` | QB | `17` | `17` | 79 | START | 79 | 96 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 108 | START | 108 | 115 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_ReadDefender` | 46 | 78 | 33 | inferred_complete_timeline |
| `Action_PullBall` | 79 | 96 | 18 | inferred_complete_timeline |
| `Action_None` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 116 | 244 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 105 | 39 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 244 | 178 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 419 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 325 | 259 | inferred_complete_timeline |
| `Action_None` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 346 | 374 | 29 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 130 | 64 | inferred_complete_timeline |
| `Action_None` | 159 | 274 | 116 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 103 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 160 | 198 | 39 | inferred_complete_timeline |
| `Action_None` | 201 | 274 | 74 | inferred_complete_timeline |
| `Action_None` | 279 | 295 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 106 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 88 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 106 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 106 | 28 | inferred_complete_timeline |
| `Action_None` | 121 | 138 | 18 | inferred_complete_timeline |
| `Action_None` | 141 | 419 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 105 | 38 | inferred_complete_timeline |
| `Action_None` | 124 | 254 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 103 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 75 | 9 | inferred_complete_timeline |
| `Action_None` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 256 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 96 | 30 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 105 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 103 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 102 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 244 | 178 | inferred_complete_timeline |
| `Action_None` | 246 | 398 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 211 | 145 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 222 | 228 | 7 | inferred_complete_timeline |
| `Action_None` | 235 | 334 | 100 | inferred_complete_timeline |
| `Action_None` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_None` | 345 | 354 | 10 | inferred_complete_timeline |
| `Action_None` | 388 | 391 | 4 | inferred_complete_timeline |
| `Action_None` | 401 | 402 | 2 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 144 | 78 | inferred_complete_timeline |
| `Action_None` | 146 | 334 | 189 | inferred_complete_timeline |
| `Action_None` | 336 | 340 | 5 | inferred_complete_timeline |
| `Action_None` | 342 | 344 | 3 | inferred_complete_timeline |
| `Action_None` | 348 | 361 | 14 | inferred_complete_timeline |
| `Action_None` | 363 | 367 | 5 | inferred_complete_timeline |
| `Action_None` | 369 | 378 | 10 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 184 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 133 | 67 | inferred_complete_timeline |
| `Action_None` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 154 | 257 | 104 | inferred_complete_timeline |
| `Action_None` | 261 | 305 | 45 | inferred_complete_timeline |
| `Action_None` | 307 | 325 | 19 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |
| `Action_None` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 355 | 10 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 382 | 383 | 2 | inferred_complete_timeline |
| `Action_None` | 388 | 412 | 25 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 93–112 | 8 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 100–274 | 99 | 8 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 125–134 | 10 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 145–419 | 248 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 161–247 | 87 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 161–419 | 170 | 7 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 161–419 | 242 | 7 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 161–276 | 114 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 161–222 | 57 | 5 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 162–267 | 102 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 162–275 | 114 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 170–236 | 46 | 9 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 173–230 | 35 | 5 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 190–195 | 6 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 221–231 | 10 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 235–275 | 30 | 6 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 239–383 | 142 | 3 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 261–272 | 12 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 270–279 | 10 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 270–339 | 58 | 4 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 292–419 | 95 | 5 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 293–295 | 3 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 296–419 | 124 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 316–358 | 29 | 4 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 316–327 | 12 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 317–320 | 4 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 319–346 | 11 | 3 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 324–326 | 3 | 1 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `58` | `86` | Position_Unknown | Team_Unknown | 327–417 | 49 | 10 | Undefined position; Undefined team |
| `59` | `87` | Position_Unknown | Team_Unknown | 327–355 | 21 | 3 | Undefined position; Undefined team |
| `60` | `88` | Position_Unknown | Team_Unknown | 327–419 | 93 | 1 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 335–417 | 68 | 4 | Undefined position; Undefined team |
| `62` | `93` | Position_Unknown | Team_Unknown | 337–388 | 52 | 1 | Undefined position; Undefined team |
| `63` | `94` | Position_Unknown | Team_Unknown | 337–355 | 19 | 1 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `65` | `98` | Position_Unknown | Team_Unknown | 346–349 | 4 | 1 | Undefined position; Undefined team |
| `66` | `101` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `67` | `103` | Position_Unknown | Team_Unknown | 353–419 | 60 | 5 | Undefined position; Undefined team |
| `68` | `104` | Position_Unknown | Team_Unknown | 353–419 | 58 | 4 | Undefined position; Undefined team |
| `69` | `106` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `70` | `107` | Position_Unknown | Team_Unknown | 357–362 | 5 | 2 | Undefined position; Undefined team |
| `71` | `108` | Position_Unknown | Team_Unknown | 360–408 | 31 | 5 | Undefined position; Undefined team |
| `72` | `114` | Position_Unknown | Team_Unknown | 379–419 | 10 | 2 | Undefined position; Undefined team |
| `73` | `115` | Position_Unknown | Team_Unknown | 380–419 | 39 | 2 | Undefined position; Undefined team |
| `74` | `116` | Position_Unknown | Team_Unknown | 381–407 | 13 | 3 | Undefined position; Undefined team |
| `75` | `121` | Position_Unknown | Team_Unknown | 384–399 | 14 | 2 | Undefined position; Undefined team |
| `76` | `122` | Position_Unknown | Team_Unknown | 385–390 | 5 | 2 | Undefined position; Undefined team |
| `77` | `124` | Position_Unknown | Team_Unknown | 387–394 | 7 | 2 | Undefined position; Undefined team |
| `78` | `125` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `79` | `128` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 58 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 58 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 116 |
| Missing visible bounding boxes during action | 227 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [67-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-374] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-257] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-305] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-325] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-412] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-244] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-398] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-211] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-334] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-334] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-367] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [46-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-73] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-198] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-274] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-270] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-231] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-351] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-385] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-408] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-384] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-396] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-241] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-385] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-397] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-175] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-276] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-226] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-267] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-200] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-275] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-378] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-272] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-279] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-311] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-324] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-357] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-376] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-325] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-358] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-370] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-388] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-407] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-395] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-417] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-388] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-355] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-363] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-392] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-407] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-402] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-370] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-387] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-407] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-399] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '78' has 1 frames without a visible bounding box.
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

</details>