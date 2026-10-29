# Play-Annotation-Generator Annotation Review — Duo_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_91`
- **Frame Range:** 0 to 448 (449 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 448
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | LB1 | defense | `20` | `20` |
| ✅ EXACT | `Action_ComboBlock` | SAF | defense | `1` | `1` |
| ✅ EXACT | `Action_ComboBlock` | WR3 | offense | `14` | `14` |
| ✅ EXACT | `Action_ComboBlock` | WR1 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR4 | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 369 |
| ✅ EXACT | `Action_BlockSecondLevel` | LB1 | `20` | `20` | 260 | START | 260 | 329 |
| ✅ EXACT | `Action_ComboBlock` | SAF | `1` | `1` | 260 | START | 260 | 329 |
| ✅ EXACT | `Action_ComboBlock` | WR3 | `14` | `14` | 260 | START | 260 | 329 |
| ✅ EXACT | `Action_ComboBlock` | WR1 | `2` | `2` | 260 | START | 260 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR4 | `5` | `5` | 260 | START | 263 | 303 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 329 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 369 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 259 | 73 | inferred_complete_timeline |
| `Action_ComboBlock` | 260 | 329 | 70 | inferred_complete_timeline |
| `Action_None` | 330 | 370 | 41 | inferred_complete_timeline |
| `Action_None` | 373 | 379 | 7 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 398 | 401 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 448 | 411 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_ComboBlock` | 260 | 329 | 70 | inferred_complete_timeline |
| `Action_None` | 330 | 379 | 50 | inferred_complete_timeline |
| `Action_None` | 381 | 448 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 249 | 138 | inferred_complete_timeline |
| `Action_ComboBlock` | 263 | 303 | 41 | inferred_complete_timeline |
| `Action_ComboBlock` | 306 | 329 | 24 | inferred_complete_timeline |
| `Action_None` | 330 | 448 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 363 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 448 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 51 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 331 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 426 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 434 | 435 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 89 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 309 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 448 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 177 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 296 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 425 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 70 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 448 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 61 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 69 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 388 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 448 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 312 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 417 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 448 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 260 | 329 | 70 | inferred_complete_timeline |
| `Action_None` | 330 | 448 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 378 | 379 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 381 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 448 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 448 | 449 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 448 | 449 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 448 | 449 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_ComboBlock` | 260 | 329 | 70 | inferred_complete_timeline |
| `Action_None` | 330 | 448 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 88 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 116 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 448 | 330 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `29` | Position_Unknown | Team_Unknown | 197–394 | 198 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 197–409 | 187 | 8 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 210–448 | 183 | 10 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 345–351 | 7 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 347–348 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 360–371 | 11 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 372–407 | 6 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 397–431 | 27 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 399–417 | 6 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 426–428 | 3 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 437–448 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 119 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-61] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-448] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-370] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-379] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-93] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-388] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-249] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [263-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-53] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-163] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-173] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-312] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-417] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-379] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-51] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-331] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-426] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-435] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-177] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-296] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-425] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-93] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-363] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-309] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-448] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-394] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-227] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-303] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-362] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-409] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-247] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-306] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-390] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-425] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-439] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-368] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-414] for track '29' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-427] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-428] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-440] for track '32' has 1 frames without a visible bounding box.
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

</details>