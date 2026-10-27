# Play-Annotation-Generator Annotation Review — Counter_325

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_325`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 71 | START | 71 | 83 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `17` | `16` | 74 | START | 84 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `21` | `20` | 74 | START | 74 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 74 | START | 74 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `18` | `17` | 74 | START | 74 | 129 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `7` | `6` | 74 | START | 74 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 83 | END | 71 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 121 | START | 121 | 422 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 422 | 302 | inferred_complete_timeline |
| `Action_BallCarry` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 436 | 449 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 449 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 449 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 267 | 197 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–446
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 446 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 95 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 74 | 170 | 97 | inferred_complete_timeline |
| `Action_None` | 171 | 449 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PullBlock` | 74 | 129 | 56 | inferred_complete_timeline |
| `Action_PullBlock` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_None` | 181 | 206 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 170 | 87 | inferred_complete_timeline |
| `Action_None` | 171 | 449 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 118 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 170 | 97 | inferred_complete_timeline |
| `Action_None` | 171 | 220 | 50 | inferred_complete_timeline |
| `Action_None` | 224 | 449 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 189 | 119 | inferred_complete_timeline |
| `Action_None` | 207 | 238 | 32 | inferred_complete_timeline |
| `Action_None` | 250 | 449 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 144 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 168 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 116 | 46 | inferred_complete_timeline |
| `Action_None` | 118 | 181 | 64 | inferred_complete_timeline |
| `Action_None` | 184 | 449 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 167 | 97 | inferred_complete_timeline |
| `Action_None` | 182 | 196 | 15 | inferred_complete_timeline |
| `Action_None` | 199 | 449 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 177 | 107 | inferred_complete_timeline |
| `Action_None` | 179 | 291 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 449 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 449 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 124 | 54 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 361 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 431 | 361 | inferred_complete_timeline |
| `Action_None` | 434 | 449 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 381 | 311 | inferred_complete_timeline |
| `Action_None` | 383 | 449 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 248 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–284 | 101 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 112–449 | 330 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 169–174 | 6 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 193–449 | 256 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 195–449 | 252 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 214–449 | 205 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 227–230 | 4 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 245–250 | 6 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 247–435 | 180 | 4 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 256–343 | 46 | 6 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 258–420 | 153 | 6 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 292–357 | 35 | 9 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 302–449 | 148 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 311–312 | 2 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 315–384 | 33 | 6 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 325–328 | 4 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 333–409 | 15 | 5 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 424–427 | 4 | 1 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 435–443 | 5 | 2 | Undefined position; Undefined team |
| `46` | `80` | Position_Unknown | Team_Unknown | 442–449 | 8 | 1 | Undefined position; Undefined team |
| `47` | `81` | Position_Unknown | Team_Unknown | 442–449 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `17` (C): Annotated start 74 != Inferred start 84
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 97 frames exceeds threshold 90 frames [start=74, end=170].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [71–83], lower_priority='Action_DownBlock' annotated_start=74, effective_Action_DownBlock_start=84.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 97 frames exceeds threshold 90 frames [start=74, end=170].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RT) duration 97 frames exceeds threshold 90 frames [start=74, end=170].
- ⚠️ Action 'Action_None' range [71-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-267] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-361] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-446] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-449] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-431] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-422] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [424-428] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [436-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [74-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [146-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-381] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-281] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-407] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-449] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-390] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-418] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-285] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-404] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-323] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-427] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-449] for track '46' has 2 frames without a visible bounding box.
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

</details>