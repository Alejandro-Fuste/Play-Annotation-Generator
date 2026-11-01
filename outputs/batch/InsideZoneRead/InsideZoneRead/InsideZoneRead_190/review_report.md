# Play-Annotation-Generator Annotation Review — InsideZoneRead_190

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_190`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `14` | `13` | 62 | START | 62 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 65 | START | 65 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `22` | `21` | 65 | START | 65 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 65 | START | 65 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 65 | START | 65 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 77 | END | 62 | 77 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `15` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `17` | `16` | 90 | START | 90 | 156 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 97 | START | 97 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `20` | 109 | START | 109 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 170 | 109 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 65 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 104 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 156 | 92 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 156 | 80 | inferred_complete_timeline |
| `Action_None` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 125 | 64 | inferred_complete_timeline |
| `Action_None` | 149 | 170 | 22 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 73 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 133 | 56 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_None` | 78 | 100 | 23 | inferred_complete_timeline |
| `Action_None` | 104 | 170 | 67 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_None` | 78 | 125 | 48 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 174 | 113 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 170 | 109 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 123 | 62 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 180 | 119 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 201 | 140 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–210 | 210 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–210 | 192 | 8 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–210 | 199 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–210 | 207 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 80–88 | 9 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 89–210 | 77 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 132–156 | 25 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 143–210 | 50 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 198–202 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 379: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 379: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 379: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 380: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Action 'Action_None' range [62-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-125] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [62-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-149] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-88] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [109-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [65-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-170] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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