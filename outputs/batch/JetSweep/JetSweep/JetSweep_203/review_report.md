# Play-Annotation-Generator Annotation Review — JetSweep_203

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_203`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 36
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `6` | `5` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `17` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `6` | `5` | 74 | START | 74 | 137 |
| ✅ EXACT | `Action_BallSnap` | LG | `21` | `20` | 108 | START | 108 | 120 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `2` | `1` | 121 | START | 121 | 212 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `12` | 121 | START | 121 | 212 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 121 | START | 121 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 121 | START | 121 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 121 | START | 121 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 121 | START | 121 | 212 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 126 | END | 108 | 126 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 133 | START | 133 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `6` | `5` | 138 | START | 138 | 207 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_SnapReceive` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_Toss` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_JetMotion` | 74 | 137 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 207 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 234 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 264 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 214 | 107 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 243 | 20 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_LeadBlock` | 121 | 212 | 92 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 129 | 22 | inferred_complete_timeline |
| `Action_None` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 212 | 92 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 107 | 54 | inferred_complete_timeline |
| `Action_BallSnap` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 212 | 56 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 212 | 92 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 212 | 92 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 145 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 212 | 57 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 151 | 44 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 159 | 52 | inferred_complete_timeline |
| `Action_None` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 254 | 147 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

None.

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Missing visible bounding boxes during action | 29 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '1' (TE2) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 92 frames exceeds threshold 90 frames [start=121, end=212].
- ⚠️ Action 'Action_None' range [108-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-254] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '19' starts at frame 121, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [121-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 121, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [121-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-129] for track '20' has 1 frames without a visible bounding box.

</details>