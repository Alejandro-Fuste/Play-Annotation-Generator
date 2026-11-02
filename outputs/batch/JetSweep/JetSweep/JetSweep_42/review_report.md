# Play-Annotation-Generator Annotation Review — JetSweep_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_42`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | defense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 9 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 124 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `1` | `0` | 69 | START | 69 | 151 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 125 | START | 125 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | `23` | `22` | 127 | START | 138 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 127 | START | 127 | 186 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 127 | START | 143 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 127 | START | 127 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 127 | START | 127 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `20` | 127 | START | 127 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 139 | END | 125 | 139 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 142 | START | 142 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `1` | `0` | 152 | START | 152 | 215 |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | `18` | `17` | 158 | START | 158 | 191 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_Toss` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 174 | 50 | inferred_complete_timeline |
| `Action_None` | 177 | 253 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 285 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 167 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 191 | 20 | inferred_complete_timeline |
| `Action_None` | 192 | 265 | 74 | inferred_complete_timeline |
| `Action_None` | 267 | 299 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 152 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 191 | 37 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_BallSnap` | 125 | 132 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 190 | 48 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–152
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 126 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 152 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 186 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 158 | 191 | 34 | inferred_complete_timeline |
| `Action_None` | 192 | 295 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 148 | 24 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 168 | 184 | 17 | inferred_complete_timeline |
| `Action_None` | 187 | 299 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_None` | 157 | 266 | 110 | inferred_complete_timeline |
| `Action_None` | 273 | 299 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 189 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 211 | 87 | inferred_complete_timeline |
| `Action_None` | 214 | 228 | 15 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 271 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–299 | 233 | 4 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–276 | 277 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 44–137 | 22 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 138–299 | 136 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 174–299 | 126 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 176–299 | 104 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 221–299 | 63 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `23` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 127 != Inferred start 143
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 85: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 86: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [125–139], lower_priority='Action_ZoneBlock' annotated_start=127, effective_Action_ZoneBlock_start=140.
- ⚠️ Action 'Action_BallCarry' range [152-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-271] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-228] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [125-132] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-190] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [138-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-267] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>