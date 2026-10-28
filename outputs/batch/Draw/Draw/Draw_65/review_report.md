# Play-Annotation-Generator Annotation Review — Draw_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_65`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 31 | START | 31 | 45 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `9` | 34 | START | 34 | 101 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `18` | 34 | START | 34 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 34 | START | 46 | 50 |
| ✅ EXACT | `Action_PassBlock` | LG | `22` | `21` | 34 | START | 34 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `6` | 34 | START | 34 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 45 | END | 31 | 45 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `20` | `19` | 50 | START | 50 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `20` | `19` | 80 | START | 80 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 50 | 79 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 203 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 389 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 73 | 43 | inferred_complete_timeline |
| `Action_None` | 76 | 162 | 87 | inferred_complete_timeline |
| `Action_None` | 167 | 248 | 82 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 389 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 389 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 359 | 329 | inferred_complete_timeline |
| `Action_None` | 362 | 379 | 18 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 182 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 350 | 320 | inferred_complete_timeline |
| `Action_None` | 354 | 366 | 13 | inferred_complete_timeline |
| `Action_None` | 370 | 386 | 17 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_None` | 102 | 244 | 143 | inferred_complete_timeline |
| `Action_None` | 247 | 264 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_None` | 102 | 123 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_None` | 102 | 246 | 145 | inferred_complete_timeline |
| `Action_None` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_None` | 264 | 314 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 85 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 102 | 389 | 288 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 71 | 41 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 131 | 230 | 100 | inferred_complete_timeline |
| `Action_None` | 233 | 389 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 100 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 69 | 39 | inferred_complete_timeline |
| `Action_None` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 123 | 254 | 132 | inferred_complete_timeline |
| `Action_None` | 256 | 308 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 87 | 57 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 107 | 77 | inferred_complete_timeline |
| `Action_None` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 152 | 31 | inferred_complete_timeline |
| `Action_None` | 155 | 248 | 94 | inferred_complete_timeline |
| `Action_None` | 250 | 291 | 42 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 389 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 353 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 389 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 389 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 389 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 354 | 324 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 77–92 | 16 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 86–89 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 105–272 | 168 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 115–249 | 135 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 122–389 | 268 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 146–204 | 59 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 147–168 | 20 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 168–243 | 28 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 184–264 | 58 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 185–278 | 63 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 198–338 | 141 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 220–389 | 160 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 272–367 | 42 | 8 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 274–366 | 81 | 4 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 375–389 | 10 | 3 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 376–389 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [31–45], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=46.
- ⚠️ Action 'Action_None' range [31-350] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-366] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-386] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-230] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-389] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-248] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-291] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-100] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-389] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-244] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-264] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-359] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-254] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-308] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-162] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-248] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-353] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-246] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-314] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-91] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-203] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-272] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-204] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-227] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-338] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-248] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-341] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-366] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '38' has 1 frames without a visible bounding box.
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

</details>