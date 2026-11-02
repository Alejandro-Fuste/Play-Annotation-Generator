# Play-Annotation-Generator Annotation Review — JetSweep_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_80`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 40
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_SealBlock` | TE2 | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `1` | `0` | 16 | START | 16 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 52 | START | 52 | 61 |
| ✅ EXACT | `Action_LeadBlock` | RB | `15` | `14` | 55 | START | 55 | 114 |
| ✅ EXACT | `Action_SealBlock` | TE2 | `6` | `5` | 55 | START | 55 | 269 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 55 | START | 62 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 55 | START | 55 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 55 | START | 55 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 55 | START | 55 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 61 | END | 52 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 66 | START | 66 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `0` | 76 | START | 76 | 204 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `4` | `3` | 81 | START | 81 | 114 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 114 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 61 | 10 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_Toss` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_LeadBlock` | 55 | 114 | 60 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_JetMotion` | 16 | 75 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 204 | 129 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 232 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 251 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SealBlock` | 55 | 269 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 114 | 60 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 61 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 80 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 81 | 114 | 34 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 114 | 60 | inferred_complete_timeline |
| `Action_None` | 115 | 269 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 83 | 32 | inferred_complete_timeline |
| `Action_None` | 88 | 225 | 138 | inferred_complete_timeline |
| `Action_None` | 233 | 269 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 82 | 31 | inferred_complete_timeline |
| `Action_None` | 88 | 269 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 77 | 26 | inferred_complete_timeline |
| `Action_None` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 125 | 74 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 246 | 195 | inferred_complete_timeline |
| `Action_None` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 260 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 112 | 61 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 100 | 49 | inferred_complete_timeline |
| `Action_None` | 105 | 134 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 182 | 131 | inferred_complete_timeline |
| `Action_None` | 186 | 222 | 37 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–269 | 266 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 15–17 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 149–269 | 121 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 221–230 | 10 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 266–269 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 55 != Inferred start 62
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 162: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [52–61], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=62.
- ⚠️ Action 'Action_BallCarry' range [76-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-232] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-251] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-260] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-182] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-225] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>