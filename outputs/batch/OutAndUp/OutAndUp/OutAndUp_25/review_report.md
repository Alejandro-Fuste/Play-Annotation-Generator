# Play-Annotation-Generator Annotation Review — OutAndUp_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_25`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_PumpFake` | RB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 18 | START | 18 | 35 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `11` | 21 | START | 36 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 21 | START | 21 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 21 | START | 21 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 21 | START | 21 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 21 | START | 21 | 103 |
| ✅ EXACT | `Action_SnapReceive` | RB | `5` | `5` | 35 | END | 18 | 35 |
| ✅ EXACT | `Action_SellOut` | WR1 | `1` | `1` | 79 | START | 79 | 95 |
| ✅ EXACT | `Action_PumpFake` | RB | `5` | `5` | 87 | START | 87 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `1` | `1` | 96 | START | 96 | 276 |
| ✅ EXACT | `Action_ThrowPass` | RB | `5` | `5` | 114 | START | 114 | 121 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 71 | 54 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 299 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 35 | 18 | inferred_complete_timeline |
| `Action_None` | 36 | 86 | 51 | inferred_complete_timeline |
| `Action_PumpFake` | 87 | 113 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SellOut` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 96 | 276 | 181 | inferred_complete_timeline |
| `Action_RunGoRoute` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_RunGoRoute` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 127 | 110 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 103 | 83 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 129 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 35 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 61 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 284 | 167 | inferred_complete_timeline |
| `Action_PassBlock` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 97 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 105 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 185 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_None` | 67 | 299 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 134 | 117 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 270 | 113 | inferred_complete_timeline |
| `Action_None` | 280 | 295 | 16 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 207 | 190 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 67 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 299 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 218 | 201 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 247 | 11 | inferred_complete_timeline |
| `Action_None` | 251 | 268 | 18 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 288 | 8 | inferred_complete_timeline |
| `Action_None` | 290 | 295 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 151 | 134 | inferred_complete_timeline |
| `Action_None` | 153 | 201 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–293 | 292 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 72–122 | 51 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 96–299 | 181 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 105–299 | 184 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 109–113 | 5 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 135–299 | 156 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 143–299 | 138 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 160–202 | 43 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 162–299 | 117 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 198–267 | 38 | 6 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 223–299 | 77 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 231–299 | 46 | 5 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 231–299 | 59 | 4 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 236–299 | 64 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 248–258 | 6 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 271–299 | 20 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 281–299 | 16 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 287–289 | 3 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 21 != Inferred start 36
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [18–35], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=36.
- ⚠️ Action 'Action_RunGoRoute' range [96-276] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [291-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [295-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-268] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-299] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-151] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-201] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-61] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-91] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-283] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [287-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-185] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-122] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-189] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-247] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-251] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-297] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-299] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>