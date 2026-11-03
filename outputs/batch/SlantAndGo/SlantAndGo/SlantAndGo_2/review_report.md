# Play-Annotation-Generator Annotation Review — SlantAndGo_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_VerticalStem` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 8 | START | 8 | 26 |
| ✅ EXACT | `Action_PassBlock` | LT | `0` | `0` | 18 | START | 18 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 18 | START | 27 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `2` | 18 | START | 18 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `4` | 18 | START | 18 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 18 | START | 18 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `9` | `9` | 26 | END | 8 | 12 |
| ✅ EXACT | `Action_VerticalStem` | Position_Unknown | `15` | `14` | 57 | START | 57 | 182 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 91 | START | 91 | 96 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 12 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 26 | 8 | inferred_complete_timeline |
| `Action_None` | 27 | 90 | 64 | inferred_complete_timeline |
| `Action_ThrowPass` | 91 | 96 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 99 | 92 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 202 | 85 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 211 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 239 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 26 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 89 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 124 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 154 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 131 | 114 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 153 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 113 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 151 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 133 | 126 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 13 | 6 | inferred_complete_timeline |
| `Action_None` | 20 | 57 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 114 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 65 | 58 | inferred_complete_timeline |
| `Action_None` | 71 | 224 | 154 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 82 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 6–15 | 10 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 20–182 | 163 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 28–112 | 80 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 97–239 | 137 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 100–239 | 139 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 117–154 | 37 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 119–239 | 116 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 130–239 | 109 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [8-65] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-124] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-202] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-26] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-13] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-133] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [8-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [91-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-114] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [8-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [57-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-160] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>