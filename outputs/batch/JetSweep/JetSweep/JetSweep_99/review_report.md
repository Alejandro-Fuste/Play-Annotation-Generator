# Play-Annotation-Generator Annotation Review — JetSweep_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | defense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | SAF2 | defense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 18 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 18 | START | 18 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 18 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 18 | START | 18 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 18 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 18 | START | 18 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 18 | START | 18 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 18 | START | 18 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 18 | START | 18 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 55 | START | 55 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 58 | START | 69 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 58 | START | 58 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 58 | START | 58 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 58 | START | 58 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 58 | START | 58 | 127 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `20` | `19` | 64 | START | 64 | 84 |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | `7` | `6` | 68 | END | 55 | 68 |
| ✅ EXACT | `Action_Toss` | SAF2 | `7` | `6` | 77 | START | 77 | 84 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 85 | START | 85 | 209 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–133
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 99 | 45 | inferred_complete_timeline |
| `Action_None` | 104 | 133 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 82 | 28 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–79
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 79 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–161
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 161 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 127 | 70 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 18–112
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 112 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 127 | 55 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 18–155
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 127 | 70 | inferred_complete_timeline |
| `Action_None` | 128 | 155 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 127 | 70 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 18–80
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 80 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 139 | 85 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 183 | 129 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–91
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 87 | 33 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–87
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 79 | 25 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 18–79
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 54 | 11 | inferred_complete_timeline |
| `Action_None` | 55 | 79 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_Toss` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 58–64 | 7 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 64–209 | 146 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 87–101 | 15 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 88–210 | 123 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 125–210 | 82 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 129–210 | 72 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 136–190 | 55 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 143–175 | 33 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 180–210 | 30 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 200: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [55–68], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=69.
- ⚠️ Action 'Action_None' range [55-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-161] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-43] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [55-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-209] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-190] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '29' has 1 frames without a visible bounding box.
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

</details>