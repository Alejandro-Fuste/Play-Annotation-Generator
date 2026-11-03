# Play-Annotation-Generator Annotation Review — OutAndUp_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_SellOut` | LB2 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | LB2 | defense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 24 | START | 24 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `10` | `10` | 27 | START | 27 | 117 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `14` | `14` | 27 | START | 30 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `2` | 27 | START | 27 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 27 | START | 27 | 82 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `17` | `17` | 29 | END | 45 | 45 |
| ✅ EXACT | `Action_SellOut` | LB2 | `1` | `1` | 56 | START | 56 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | LB2 | `1` | `1` | 97 | START | 97 | 97 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `17` | `17` | 118 | START | 118 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 127 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 86 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 110 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 138 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 153 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 136 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 117 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 141 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 161 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 82 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 132 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 162 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 81 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 153 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 166 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 53 | 30 | inferred_complete_timeline |
| `Action_None` | 63 | 173 | 111 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SellOut` | 56 | 96 | 41 | inferred_complete_timeline |
| `Action_RunGoRoute` | 97 | 97 | 1 | inferred_complete_timeline |
| `Action_RunGoRoute` | 99 | 176 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 162 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 73 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 138 | 115 | inferred_complete_timeline |
| `Action_None` | 142 | 190 | 49 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–75 | 76 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 3–63 | 28 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–37 | 28 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 45–164 | 118 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 49–86 | 37 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 81–166 | 49 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 88–100 | 13 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 111–169 | 54 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 119–164 | 45 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–165 | 41 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 127–153 | 18 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 132–154 | 23 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 134–167 | 33 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 154–178 | 24 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 159–210 | 42 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `14` (C): Annotated start 27 != Inferred start 30
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [24–29], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=30.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=45, end=29. Clamping end to start.
- ⚠️ Action 'Action_None' range [24-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' for track '1' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunGoRoute' range [97-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [99-176] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-153] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-127] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-98] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-173] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-166] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-34] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-153] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-154] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>