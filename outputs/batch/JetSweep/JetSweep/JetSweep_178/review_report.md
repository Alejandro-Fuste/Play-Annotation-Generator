# Play-Annotation-Generator Annotation Review — JetSweep_178

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_178`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `6` | 47 | START | 47 | 59 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `20` | `18` | 49 | START | 49 | 77 |
| ✅ EXACT | `Action_LeadBlock` | RB | `15` | `15` | 51 | START | 51 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 51 | START | 51 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 51 | START | 51 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 51 | START | 51 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `6` | 51 | START | 60 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 59 | END | 47 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `14` | `14` | 66 | START | 66 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `18` | 80 | START | 80 | 81 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 92 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_Toss` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_Toss` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_None` | 80 | 111 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_LeadBlock` | 51 | 92 | 42 | inferred_complete_timeline |
| `Action_None` | 93 | 124 | 32 | inferred_complete_timeline |
| `Action_None` | 127 | 172 | 46 | inferred_complete_timeline |
| `Action_None` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 153 | 107 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 185 | 15 | inferred_complete_timeline |
| `Action_None` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 73 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 58 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 84 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 93 | 93 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 92 | 42 | inferred_complete_timeline |
| `Action_None` | 93 | 239 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 239 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 140 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 106 | 60 | inferred_complete_timeline |
| `Action_None` | 108 | 128 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 196 | 150 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 16–239 | 184 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 18–84 | 67 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 49–239 | 186 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 63–239 | 176 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 81–134 | 50 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 91–239 | 147 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 115–239 | 104 | 7 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 121–239 | 117 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 131–239 | 109 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 207–217 | 11 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 358: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [47–59], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=60.
- ⚠️ Action 'Action_None' range [47-196] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-106] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-153] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-185] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 93, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [93-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 93, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [93-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [66-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-111] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-75] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [49-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-197] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-108] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>