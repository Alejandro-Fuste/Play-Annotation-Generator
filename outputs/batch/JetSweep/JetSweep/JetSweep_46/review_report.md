# Play-Annotation-Generator Annotation Review — JetSweep_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_46`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_LeadBlock` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE2 | defense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 76 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `2` | `1` | 44 | START | 44 | 107 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 77 | START | 77 | 90 |
| ❌ MISSING SEGMENT | `Action_LeadBlock` | RB | `15` | `14` | 83 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 83 | START | 98 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 83 | START | 83 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 83 | START | 83 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `19` | 83 | START | 83 | 85 |
| ✅ EXACT | `Action_SnapReceive` | RB | `15` | `14` | 92 | END | 77 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | RB | `15` | `14` | 96 | START | 96 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `2` | `1` | 108 | START | 108 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE2 | `12` | `11` | 108 | START | 108 | 137 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_Toss` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_Toss` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 228 | 121 | inferred_complete_timeline |
| `Action_None` | 231 | 247 | 17 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 266 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_JetMotion` | 44 | 107 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 113 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 151 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 208 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_None` | 164 | 214 | 51 | inferred_complete_timeline |
| `Action_None` | 220 | 236 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 163 | 46 | inferred_complete_timeline |
| `Action_None` | 164 | 259 | 96 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 107 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 163 | 51 | inferred_complete_timeline |
| `Action_None` | 164 | 269 | 106 | inferred_complete_timeline |

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
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 165 | 89 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 108 | 137 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 139 | 163 | 25 | inferred_complete_timeline |
| `Action_None` | 164 | 269 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 99 | 23 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 149 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 214 | 138 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 121–269 | 149 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 127–269 | 143 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 141–269 | 127 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 142–269 | 118 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 148–269 | 118 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 236–269 | 24 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_LeadBlock` on target `15` (RB)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [77–92], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=93.
- ⚠️ Segment 'Action_LeadBlock' for track '14' has invalid range: start=83, end=76. Clamping end to start.
- ⚠️ Action 'Action_None' range [77-266] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-208] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-214] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [77-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-259] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [108-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-269] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [96-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-247] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>