# Play-Annotation-Generator Annotation Review — RPO_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `37` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 52 | START | 52 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `10` | 52 | START | 52 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 52 | START | 52 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `2` | 52 | START | 52 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 52 | START | 52 | 114 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `3` | 62 | START | 62 | 70 |
| ✅ EXACT | `Action_PullBall` | QB | `3` | `3` | 71 | START | 71 | 80 |
| ✅ EXACT | `Action_ThrowPass` | QB | `3` | `3` | 110 | START | 110 | 120 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 61 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 109 | 29 | inferred_complete_timeline |
| `Action_ThrowPass` | 110 | 120 | 11 | inferred_complete_timeline |
| `Action_None` | 121 | 133 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 120 | 69 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 120 | 69 | inferred_complete_timeline |
| `Action_None` | 121 | 134 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 114 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 102 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 120 | 69 | inferred_complete_timeline |
| `Action_None` | 121 | 127 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 130 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 130 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 135 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 89 | 39 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 119 | 133 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 113 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_None` | 84 | 135 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–130 | 99 | 5 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 108–129 | 22 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 113–123 | 11 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `19` | `36` | Position_Unknown | Team_Unknown | 136–140 | 5 | 1 | Undefined position; Undefined team |
| `20` | `37` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `21` | `38` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `22` | `39` | Position_Unknown | Team_Unknown | 136–143 | 8 | 1 | Undefined position; Undefined team |
| `23` | `40` | Position_Unknown | Team_Unknown | 136–146 | 11 | 1 | Undefined position; Undefined team |
| `24` | `44` | Position_Unknown | Team_Unknown | 144–180 | 37 | 1 | Undefined position; Undefined team |
| `25` | `45` | Position_Unknown | Team_Unknown | 144–146 | 3 | 1 | Undefined position; Undefined team |
| `26` | `46` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |
| `27` | `47` | Position_Unknown | Team_Unknown | 172–180 | 9 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [51-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 51, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [51-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-135] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-107] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>