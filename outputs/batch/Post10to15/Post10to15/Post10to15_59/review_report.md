# Play-Annotation-Generator Annotation Review — Post10to15_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_59`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `21` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 21 | START | 21 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 24 | START | 40 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 24 | START | 24 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 24 | START | 24 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 24 | START | 24 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | `21` | `21` | 39 | START | 39 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 39 | END | 21 | 39 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 78 | START | 78 | 87 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_None` | 40 | 77 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 161 | 74 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 64 | 44 | inferred_complete_timeline |
| `Action_None` | 67 | 123 | 57 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_RunPostRoute` | 39 | 155 | 117 | inferred_complete_timeline |
| `Action_RunPostRoute` | 157 | 180 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 71 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 116 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 125 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 88 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 170 | 76 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 116 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 146 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 180 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 134 | 114 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 175 | 155 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 158 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 159 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 167 | 147 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–125 | 126 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 87–180 | 79 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 133–180 | 47 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 173–176 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 62: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [21–39], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=40.
- ⚠️ Action 'Action_None' range [21-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-134] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-108] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-123] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-161] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-88] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-170] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-146] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [39-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [157-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '25' has 1 frames without a visible bounding box.
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

</details>