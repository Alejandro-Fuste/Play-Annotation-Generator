# Play-Annotation-Generator Annotation Review — JetSweep_215

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_215`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `19` | `18` | 1 | START | 1 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 13 | START | 13 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `3` | `2` | 14 | START | 14 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 14 | START | 14 | 150 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 14 | START | 26 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 14 | START | 14 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 14 | START | 14 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 14 | START | 14 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 25 | END | 13 | 25 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 32 | START | 32 | 35 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `19` | `18` | 36 | START | 36 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 25 | 13 | inferred_complete_timeline |
| `Action_None` | 26 | 31 | 6 | inferred_complete_timeline |
| `Action_Toss` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_None` | 36 | 210 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 107 | 95 | inferred_complete_timeline |
| `Action_None` | 116 | 175 | 60 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 1 | 35 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 36 | 139 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 187 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LeadBlock` | 14 | 92 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 94 | 125 | 32 | inferred_complete_timeline |
| `Action_LeadBlock` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 150 | 137 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 150 | 137 | inferred_complete_timeline |
| `Action_None` | 151 | 184 | 34 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 25 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 150 | 125 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 150 | 137 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 108 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 150 | 31 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 179 | 167 | inferred_complete_timeline |
| `Action_None` | 184 | 199 | 16 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 89 | 77 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 118 | 106 | inferred_complete_timeline |
| `Action_None` | 128 | 159 | 32 | inferred_complete_timeline |
| `Action_None` | 165 | 184 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 199 | 187 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 111 | 99 | inferred_complete_timeline |
| `Action_None` | 120 | 188 | 69 | inferred_complete_timeline |
| `Action_None` | 190 | 208 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–63 | 64 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 163–210 | 46 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 174–177 | 4 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 186–210 | 25 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 14 != Inferred start 26
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 431: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '2' (TE) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [13–25], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=26.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
- ⚠️ Action 'Action_None' range [13-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [14-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [94-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-108] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-199] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-208] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-184] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [36-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>