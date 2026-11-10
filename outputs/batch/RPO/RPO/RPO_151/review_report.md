# Play-Annotation-Generator Annotation Review — RPO_151

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `RPO_151`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 68
- **Ball Tracks:** 0
- **Action Segments:** 211
- **Validation Warnings:** 298
- **Validation Errors:** 1
- **Overall Status:** FAILED
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `5` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 185
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | WR3 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 382 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 72 | START | 72 | 92 |
| ✅ EXACT | `Action_PullBall` | QB | `6` | `6` | 93 | START | 93 | 116 |
| ✅ EXACT | `Action_ThrowPass` | WR3 | `3` | `3` | 138 | START | 138 | 144 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ReadDefender` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_PullBall` | 93 | 116 | 24 | inferred_complete_timeline |
| `Action_None` | 117 | 140 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 261 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 389 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 382 | 383 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_ThrowPass` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 278 | 134 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 287 | 297 | 11 | inferred_complete_timeline |
| `Action_None` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_None` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_None` | 317 | 389 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 165 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 262 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 332 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 234 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 253 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 237 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 157 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 360 | 361 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 211 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 141 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 254 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 261 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 289 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 319 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 360 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 376 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 262 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 271 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 330 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 372 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 383 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–230 | 231 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 58–69 | 9 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 96–234 | 110 | 8 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 115–231 | 99 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 135–234 | 91 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 135–140 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 138–221 | 57 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 155–235 | 81 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 171–236 | 62 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 193–244 | 46 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 194–244 | 44 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 201–236 | 36 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 226–236 | 10 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 232–238 | 7 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 240–242 | 3 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 242–388 | 93 | 8 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 242–348 | 98 | 4 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 242–322 | 38 | 7 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 246–268 | 8 | 3 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 248–311 | 58 | 4 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 249–389 | 113 | 7 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 250–374 | 119 | 5 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 251–389 | 139 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 251–348 | 86 | 5 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 260–389 | 126 | 3 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 272–389 | 116 | 3 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 278–368 | 60 | 10 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 282–333 | 52 | 1 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 285–289 | 5 | 1 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 288–300 | 6 | 3 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 301–323 | 23 | 1 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 303–330 | 18 | 3 | Undefined position; Undefined team |
| `60` | `92` | Position_Unknown | Team_Unknown | 306–389 | 50 | 6 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 326–357 | 12 | 4 | Undefined position; Undefined team |
| `62` | `100` | Position_Unknown | Team_Unknown | 331–335 | 5 | 1 | Undefined position; Undefined team |
| `63` | `101` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `64` | `106` | Position_Unknown | Team_Unknown | 369–379 | 9 | 3 | Undefined position; Undefined team |
| `65` | `107` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `66` | `108` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `67` | `110` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 47 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 47 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LT', 'RG', 'RT'].

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 94 |
| Missing visible bounding boxes during action | 202 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 276: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-382] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-123] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-138] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-360] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-377] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-389] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-237] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-376] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-271] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-330] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-372] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-383] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-141] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-162] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-254] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-289] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-319] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-234] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-332] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-128] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-157] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-231] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-141] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-157] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-234] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-208] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-221] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-227] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-236] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-236] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-257] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-276] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-313] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-368] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-388] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-261] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-348] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-287] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-265] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-285] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-304] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-311] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-253] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-291] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-314] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-329] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-328] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-333] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-344] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-359] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-374] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-389] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-276] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-344] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-267] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-297] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-389] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-279] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-389] for track '51' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-280] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-291] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-309] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-329] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-338] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-348] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-362] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-368] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-333] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-289] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-323] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-330] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-313] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-336] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-346] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-368] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-349] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-354] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-335] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-370] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-374] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-379] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>