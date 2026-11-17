# Play-Annotation-Generator Annotation Review — Power_324

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_324`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 140
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 5 | START | 5 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 5 | START | 5 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 5 | START | 5 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `13` | `Group` | 5 | START | 5 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 5 | START | 5 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 5 | START | 5 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 5 | START | 5 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 5 | START | 5 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `6` | 39 | START | 39 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `7` | `7` | 39 | START | 39 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `4` | 39 | START | 39 | 40 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–140
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 43 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 140 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–81
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 41 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 50 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 81 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–99
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 39 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 64 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 36 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 97 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 133 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–237
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 54 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_None` | 87 | 237 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–142
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 52 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 86 | 21 | inferred_complete_timeline |
| `Action_None` | 87 | 142 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–162
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 162 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–64
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 51 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 64 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–191
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 7 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 103 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 125 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 161 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 191 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–99
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 57 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 202 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 233 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–107
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 35 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 107 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 75 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 182 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 202 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 233 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 243 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–81
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 34 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 81 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 5–264 | 256 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 5–269 | 262 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 5–149 | 129 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 22–23 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 46–269 | 224 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 68–137 | 70 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 80–125 | 45 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 84–269 | 180 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 86–94 | 9 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 98–269 | 172 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 101–269 | 151 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 107–269 | 163 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 114–269 | 156 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 124–269 | 100 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 151–263 | 90 | 10 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 163–269 | 107 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 164–269 | 87 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 648: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [5-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-51] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-220] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-34] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-65] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-81] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [39-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [42-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [58-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-36] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-147] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [39-52] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [39-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [56-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-75] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-215] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-149] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-39] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-215] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-57] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-103] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-125] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-137] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-194] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-216] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-202] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-216] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-253] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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