# Play-Annotation-Generator Annotation Review — RPO_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_47`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `14` | `14` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 13 | START | 13 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 13 | START | 13 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 13 | START | 13 | 127 |
| ✅ EXACT | `Action_RunBlock` | RT | `11` | `11` | 129 | START | 129 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 129 | START | 129 | 166 |
| ✅ EXACT | `Action_RunBlock` | LT | `17` | `17` | 129 | START | 129 | 175 |
| ⚠️ START CHANGED | `Action_RunBlock` | RG | `20` | `20` | 129 | START | 132 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 129 | START | 129 | 134 |
| ✅ EXACT | `Action_ReadDefender` | RB | `14` | `14` | 130 | START | 130 | 143 |
| ✅ EXACT | `Action_PullBall` | RB | `14` | `14` | 144 | START | 144 | 155 |
| ✅ EXACT | `Action_ThrowPass` | RB | `14` | `14` | 166 | START | 166 | 175 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 419 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_PullBall` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 165 | 10 | inferred_complete_timeline |
| `Action_ThrowPass` | 166 | 175 | 10 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |
| `Action_None` | 301 | 330 | 30 | inferred_complete_timeline |
| `Action_None` | 333 | 419 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–376
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 376 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–416
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 416 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 280 | 153 | inferred_complete_timeline |
| `Action_None` | 282 | 357 | 76 | inferred_complete_timeline |
| `Action_None` | 373 | 419 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 419 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 175 | 47 | inferred_complete_timeline |
| `Action_None` | 176 | 397 | 222 | inferred_complete_timeline |
| `Action_None` | 400 | 419 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–153
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 166 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 175 | 175 | 1 | inferred_complete_timeline |
| `Action_None` | 176 | 419 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 125 | 113 | inferred_complete_timeline |
| `Action_RunBlock` | 132 | 175 | 44 | inferred_complete_timeline |
| `Action_None` | 176 | 419 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 128 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 175 | 47 | inferred_complete_timeline |
| `Action_None` | 176 | 419 | 244 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 293 | 166 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 394 | 77 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 419 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 279 | 152 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 419 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–406
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 250 | 123 | inferred_complete_timeline |
| `Action_None` | 252 | 335 | 84 | inferred_complete_timeline |
| `Action_None` | 338 | 399 | 62 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–177
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 177 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–196
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 196 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 357 | 230 | inferred_complete_timeline |
| `Action_None` | 359 | 364 | 6 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–409
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 403 | 276 | inferred_complete_timeline |
| `Action_None` | 408 | 409 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 280 | 153 | inferred_complete_timeline |
| `Action_None` | 283 | 419 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–406
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 313 | 186 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_None` | 326 | 406 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 275 | 148 | inferred_complete_timeline |
| `Action_None` | 283 | 350 | 68 | inferred_complete_timeline |
| `Action_None` | 352 | 354 | 3 | inferred_complete_timeline |
| `Action_None` | 357 | 419 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–313
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 127 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 284 | 157 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 313 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 191–337 | 146 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 203–419 | 214 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 207–231 | 7 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 226–419 | 191 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 247–250 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 272–360 | 50 | 8 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 318–322 | 5 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 318–341 | 17 | 3 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 325–419 | 32 | 7 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 336–419 | 47 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 353–389 | 37 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 374–376 | 3 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 383–405 | 19 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 394–419 | 23 | 2 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 411–419 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (2 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `20` (RG): Annotated start 129 != Inferred start 132
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 89 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [128-419] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-284] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-280] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-335] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-399] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-357] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-293] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-394] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-357] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-364] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-419] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-416] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 176, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [176-419] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-403] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-330] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-350] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-376] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-397] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-313] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-406] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-419] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [140-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-338] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-323] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-323] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-343] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-351] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-403] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-376] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-389] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-399] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-419] for track '42' has 1 frames without a visible bounding box.
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

</details>