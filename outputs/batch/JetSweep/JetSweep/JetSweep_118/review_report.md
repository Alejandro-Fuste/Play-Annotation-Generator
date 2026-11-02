# Play-Annotation-Generator Annotation Review — JetSweep_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_118`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_SealBlock` | TE1 | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `7` | `6` | 6 | START | 6 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 34 | START | 34 | 48 |
| ✅ EXACT | `Action_SealBlock` | TE1 | `21` | `20` | 35 | START | 35 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 35 | START | 35 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 35 | START | 49 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `19` | 35 | START | 35 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 35 | START | 35 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 48 | END | 34 | 48 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 51 | START | 51 | 59 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `7` | `6` | 60 | START | 60 | 209 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_Toss` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 194 | 135 | inferred_complete_timeline |
| `Action_None` | 196 | 205 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 195 | 162 | inferred_complete_timeline |
| `Action_None` | 198 | 202 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_JetMotion` | 6 | 59 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 209 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SealBlock` | 35 | 194 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 105 | 71 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 105 | 52 | inferred_complete_timeline |
| `Action_None` | 106 | 174 | 69 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 105 | 71 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 64 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 74 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 58 | 25 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 80 | 47 | inferred_complete_timeline |
| `Action_None` | 86 | 210 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 172 | 139 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 173 | 140 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 119 | 86 | inferred_complete_timeline |
| `Action_None` | 122 | 151 | 30 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 210 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 191 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 149 | 116 | inferred_complete_timeline |
| `Action_None` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–83 | 57 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–68 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 99–210 | 112 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 110–210 | 95 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 165–171 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 238: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_ZoneBlock' annotated_start=35, effective_Action_ZoneBlock_start=49.
- ⚠️ Action 'Action_None' range [34-173] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-149] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-209] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-80] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-172] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-151] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-191] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-52] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [35-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '27' has 1 frames without a visible bounding box.
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

</details>