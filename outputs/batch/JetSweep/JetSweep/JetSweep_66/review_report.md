# Play-Annotation-Generator Annotation Review — JetSweep_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_66`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `11` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `5` | `4` | 31 | START | 31 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 72 | START | 72 | 83 |
| ✅ EXACT | `Action_LeadBlock` | TE | `9` | `8` | 73 | START | 73 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `14` | 73 | START | 73 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 73 | START | 86 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 73 | START | 73 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 73 | START | 73 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 73 | START | 73 | 128 |
| ✅ EXACT | `Action_SnapReceive` | RB | `8` | `7` | 84 | END | 72 | 84 |
| ✅ EXACT | `Action_Toss` | RB | `8` | `7` | 90 | START | 90 | 100 |
| ✅ EXACT | `Action_BallCarry` | WR | `5` | `4` | 101 | START | 101 | 269 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `21` | `20` | 101 | START | 101 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 72 | 84 | 13 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_Toss` | 90 | 100 | 11 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_JetMotion` | 31 | 70 | 40 | inferred_complete_timeline |
| `Action_JetMotion` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 262 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_LeadBlock` | 73 | 128 | 56 | inferred_complete_timeline |
| `Action_None` | 129 | 145 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 128 | 56 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 100 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 101 | 128 | 28 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 269 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_BallSnap` | 72 | 83 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 128 | 34 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 128 | 56 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 128 | 56 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 264 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 103 | 32 | inferred_complete_timeline |
| `Action_None` | 107 | 124 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 142 | 71 | inferred_complete_timeline |
| `Action_None` | 145 | 158 | 14 | inferred_complete_timeline |
| `Action_None` | 162 | 252 | 91 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 269 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 181 | 110 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–269 | 268 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 146–158 | 12 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 166–269 | 104 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 169–269 | 55 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 194–267 | 69 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 209–269 | 57 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 35 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 133: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [72–84], lower_priority='Action_ZoneBlock' annotated_start=73, effective_Action_ZoneBlock_start=85.
- ⚠️ Action 'Action_None' range [72-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [31-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-269] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-262] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-252] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-181] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [72-83] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-213] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-244] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>