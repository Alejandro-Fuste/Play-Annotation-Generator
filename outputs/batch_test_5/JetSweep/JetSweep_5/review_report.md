# TapeVision Annotation Review — JetSweep_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_5`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `1` | `0` |
| ✅ EXACT | `Action_LeadBlock` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `1` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `3` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_JetMotion` | WR | `1` | `0` | 58 | START | 58 | 116 |
| ✅ EXACT | `Action_LeadBlock` | QB | `8` | `7` | 87 | START | 87 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 88 | START | 88 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 89 | START | 89 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 89 | START | 89 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 89 | START | 104 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 89 | START | 89 | 166 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 101 | END | 88 | 101 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 107 | START | 107 | 116 |
| ✅ EXACT | `Action_BallCarry` | WR | `1` | `0` | 117 | START | 117 | 224 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `19` | `18` | 136 | START | 136 | 166 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `12` | `11` | 166 | BOUNDARY | 118 | 166 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `19` | `18` | 166 | BOUNDARY | 136 | 166 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `22` | `21` | 166 | BOUNDARY | N/A | 166 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `3` | `2` | 166 | BOUNDARY | 89 | 166 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_LeadBlock` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_Toss` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 188 | 72 | inferred_complete_timeline |
| `Action_None` | 192 | 316 | 125 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 127 | 40 | inferred_complete_timeline |
| `Action_None` | 129 | 308 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_JetMotion` | 58 | 116 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 224 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 246 | 159 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 307 | 220 | inferred_complete_timeline |
| `Action_None` | 309 | 325 | 17 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 106 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 112 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 138 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 116 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 166 | 49 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 166 | 78 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 110 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 136 | 166 | 31 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 116 | 29 | inferred_complete_timeline |
| `Action_None` | 119 | 329 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 147 | 60 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LDE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 160 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 292 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 133 | 46 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 329 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 153 | 66 | inferred_complete_timeline |
| `Action_None` | 162 | 176 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 234 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 303 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–184 | 172 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 45–61 | 17 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 108–329 | 222 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 113–114 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 117–126 | 5 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 129–329 | 174 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 169–329 | 161 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 175–329 | 155 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 189–235 | 17 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 198–329 | 117 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 208–329 | 116 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 238–273 | 36 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 243–329 | 42 | 7 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 252–329 | 78 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 261–268 | 6 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 310–329 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 12: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [88–101], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=102.
- ⚠️ Action 'Action_BallCarry' range [117-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-188] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-316] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-292] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-116] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-166] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-303] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-307] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [88-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-61] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-260] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-284] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-329] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-329] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-273] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-329] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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