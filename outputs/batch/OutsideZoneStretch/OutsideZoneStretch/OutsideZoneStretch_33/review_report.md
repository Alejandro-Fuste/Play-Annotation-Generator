# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_33`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 102
- **Ball Tracks:** 0
- **Action Segments:** 259
- **Validation Warnings:** 420
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 244
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 64 | START | 64 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 64 | START | 64 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 64 | START | 64 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 64 | START | 64 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 64 | START | 64 | 115 |
| ✅ EXACT | `Action_PressEdge` | RB | `9` | `9` | 68 | START | 68 | 128 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 89 | START | 89 | 100 |

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
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 88 | 30 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 152 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PressEdge` | 68 | 128 | 61 | inferred_complete_timeline |
| `Action_None` | 129 | 241 | 113 | inferred_complete_timeline |
| `Action_None` | 243 | 419 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 115 | 52 | inferred_complete_timeline |
| `Action_None` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_None` | 137 | 355 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 115 | 52 | inferred_complete_timeline |
| `Action_None` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_None` | 131 | 168 | 38 | inferred_complete_timeline |
| `Action_None` | 170 | 367 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 115 | 32 | inferred_complete_timeline |
| `Action_None` | 128 | 227 | 100 | inferred_complete_timeline |
| `Action_None` | 230 | 373 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 137 | 22 | inferred_complete_timeline |
| `Action_None` | 149 | 175 | 27 | inferred_complete_timeline |
| `Action_None` | 177 | 382 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 115 | 52 | inferred_complete_timeline |
| `Action_None` | 116 | 356 | 241 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 397 | 398 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 142 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 351 | 352 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 392 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 182 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 197 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–413
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 413 | 414 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 411 | 194 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–392 | 392 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–342 | 337 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 50–59 | 7 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 95–413 | 311 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 108–419 | 304 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 109–396 | 284 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 116–378 | 263 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 120–419 | 300 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 125–131 | 5 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 152–351 | 197 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 157–369 | 192 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 244–339 | 26 | 5 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 249–304 | 29 | 3 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 253–313 | 22 | 7 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 265–381 | 117 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 265–352 | 86 | 2 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 266–339 | 67 | 4 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 266–289 | 24 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 266–340 | 28 | 3 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 267–333 | 53 | 5 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 267–275 | 7 | 2 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 269–311 | 32 | 2 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 271–361 | 83 | 3 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 271–366 | 76 | 4 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 272–356 | 66 | 4 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 275–287 | 7 | 2 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 279–352 | 17 | 6 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 281–308 | 26 | 2 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 285–305 | 11 | 2 | Undefined position; Undefined team |
| `47` | `80` | Position_Unknown | Team_Unknown | 286–349 | 61 | 3 | Undefined position; Undefined team |
| `48` | `82` | Position_Unknown | Team_Unknown | 288–350 | 61 | 3 | Undefined position; Undefined team |
| `49` | `85` | Position_Unknown | Team_Unknown | 290–337 | 31 | 4 | Undefined position; Undefined team |
| `50` | `87` | Position_Unknown | Team_Unknown | 292–329 | 15 | 5 | Undefined position; Undefined team |
| `51` | `90` | Position_Unknown | Team_Unknown | 298–335 | 29 | 2 | Undefined position; Undefined team |
| `52` | `93` | Position_Unknown | Team_Unknown | 302–349 | 45 | 3 | Undefined position; Undefined team |
| `53` | `94` | Position_Unknown | Team_Unknown | 303–353 | 40 | 8 | Undefined position; Undefined team |
| `54` | `95` | Position_Unknown | Team_Unknown | 303–357 | 54 | 2 | Undefined position; Undefined team |
| `55` | `96` | Position_Unknown | Team_Unknown | 303–343 | 34 | 6 | Undefined position; Undefined team |
| `56` | `98` | Position_Unknown | Team_Unknown | 305–334 | 16 | 5 | Undefined position; Undefined team |
| `57` | `101` | Position_Unknown | Team_Unknown | 308–370 | 63 | 1 | Undefined position; Undefined team |
| `58` | `102` | Position_Unknown | Team_Unknown | 310–320 | 11 | 1 | Undefined position; Undefined team |
| `59` | `103` | Position_Unknown | Team_Unknown | 310–352 | 28 | 5 | Undefined position; Undefined team |
| `60` | `104` | Position_Unknown | Team_Unknown | 311–334 | 24 | 1 | Undefined position; Undefined team |
| `61` | `107` | Position_Unknown | Team_Unknown | 316–318 | 3 | 1 | Undefined position; Undefined team |
| `62` | `108` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `63` | `109` | Position_Unknown | Team_Unknown | 317–332 | 6 | 3 | Undefined position; Undefined team |
| `64` | `111` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `65` | `112` | Position_Unknown | Team_Unknown | 326–348 | 18 | 3 | Undefined position; Undefined team |
| `66` | `113` | Position_Unknown | Team_Unknown | 330–332 | 3 | 1 | Undefined position; Undefined team |
| `67` | `114` | Position_Unknown | Team_Unknown | 331–355 | 14 | 4 | Undefined position; Undefined team |
| `68` | `115` | Position_Unknown | Team_Unknown | 334–403 | 60 | 7 | Undefined position; Undefined team |
| `69` | `117` | Position_Unknown | Team_Unknown | 335–337 | 3 | 1 | Undefined position; Undefined team |
| `70` | `118` | Position_Unknown | Team_Unknown | 336–342 | 7 | 1 | Undefined position; Undefined team |
| `71` | `119` | Position_Unknown | Team_Unknown | 339–360 | 17 | 2 | Undefined position; Undefined team |
| `72` | `123` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `73` | `126` | Position_Unknown | Team_Unknown | 348–375 | 28 | 1 | Undefined position; Undefined team |
| `74` | `128` | Position_Unknown | Team_Unknown | 351–381 | 24 | 4 | Undefined position; Undefined team |
| `75` | `130` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `76` | `131` | Position_Unknown | Team_Unknown | 357–411 | 49 | 4 | Undefined position; Undefined team |
| `77` | `137` | Position_Unknown | Team_Unknown | 362–416 | 48 | 4 | Undefined position; Undefined team |
| `78` | `138` | Position_Unknown | Team_Unknown | 363–411 | 37 | 3 | Undefined position; Undefined team |
| `79` | `144` | Position_Unknown | Team_Unknown | 366–391 | 26 | 1 | Undefined position; Undefined team |
| `80` | `146` | Position_Unknown | Team_Unknown | 367–385 | 19 | 1 | Undefined position; Undefined team |
| `81` | `147` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `82` | `148` | Position_Unknown | Team_Unknown | 367–390 | 24 | 1 | Undefined position; Undefined team |
| `83` | `149` | Position_Unknown | Team_Unknown | 369–371 | 3 | 1 | Undefined position; Undefined team |
| `84` | `151` | Position_Unknown | Team_Unknown | 372–390 | 19 | 1 | Undefined position; Undefined team |
| `85` | `152` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `86` | `153` | Position_Unknown | Team_Unknown | 374–399 | 24 | 2 | Undefined position; Undefined team |
| `87` | `154` | Position_Unknown | Team_Unknown | 374–389 | 9 | 3 | Undefined position; Undefined team |
| `88` | `155` | Position_Unknown | Team_Unknown | 376–397 | 22 | 1 | Undefined position; Undefined team |
| `89` | `157` | Position_Unknown | Team_Unknown | 376–385 | 6 | 3 | Undefined position; Undefined team |
| `90` | `158` | Position_Unknown | Team_Unknown | 377–409 | 7 | 2 | Undefined position; Undefined team |
| `91` | `159` | Position_Unknown | Team_Unknown | 378–419 | 30 | 4 | Undefined position; Undefined team |
| `92` | `162` | Position_Unknown | Team_Unknown | 379–407 | 29 | 1 | Undefined position; Undefined team |
| `93` | `163` | Position_Unknown | Team_Unknown | 379–394 | 13 | 2 | Undefined position; Undefined team |
| `94` | `164` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `95` | `165` | Position_Unknown | Team_Unknown | 380–388 | 4 | 2 | Undefined position; Undefined team |
| `96` | `166` | Position_Unknown | Team_Unknown | 380–385 | 4 | 2 | Undefined position; Undefined team |
| `97` | `167` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `98` | `172` | Position_Unknown | Team_Unknown | 392–395 | 4 | 1 | Undefined position; Undefined team |
| `99` | `173` | Position_Unknown | Team_Unknown | 394–405 | 10 | 2 | Undefined position; Undefined team |
| `100` | `175` | Position_Unknown | Team_Unknown | 405–407 | 3 | 1 | Undefined position; Undefined team |
| `101` | `176` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 86 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 86 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 172 |
| Missing visible bounding boxes during action | 246 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 68: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-392] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-392] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-413] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-397] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-367] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-137] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-382] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-411] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-356] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-123] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-355] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-74] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-115] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-413] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-397] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-396] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-378] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-419] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-346] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-247] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-276] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-258] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-278] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-258] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-309] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-290] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-352] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-339] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-290] for track '36' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-340] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-308] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-333] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-275] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-277] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-311] for track '39' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-279] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-357] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-284] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-302] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-327] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-366] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-348] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-356] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-279] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-285] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-302] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-308] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-305] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-339] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-345] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-307] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-350] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-322] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-337] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-324] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-304] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-345] for track '52' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-318] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-326] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-344] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-353] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-330] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-357] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-326] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-330] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-338] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-314] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-322] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-370] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-320] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-329] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-337] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-343] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-352] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-334] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-337] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-348] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-339] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-352] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-349] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-379] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-384] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-389] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-395] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-403] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-337] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-342] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-360] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-375] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-358] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-375] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-381] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-365] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-396] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-411] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-399] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-407] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-416] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-387] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-396] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-411] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-391] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-385] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-369] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-390] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-390] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-393] for track '86' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-382] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-397] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-409] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-385] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-400] for track '91' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-407] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-389] for track '93' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-395] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-401] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-407] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.

</details>