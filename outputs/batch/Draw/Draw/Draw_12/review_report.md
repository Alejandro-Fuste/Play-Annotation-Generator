# Play-Annotation-Generator Annotation Review — Draw_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 0 | START | 0 | 41 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `21` | `17` | 42 | START | 66 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `11` | 45 | START | 45 | 139 |
| ✅ EXACT | `Action_PassBlock` | LT | `13` | `12` | 45 | START | 45 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `3` | 45 | START | 45 | 57 |
| ✅ EXACT | `Action_PassBlock` | RG | `7` | `6` | 45 | START | 45 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `16` | `15` | 48 | END | 42 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | `16` | `15` | 52 | START | 55 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `16` | `15` | 83 | START | 83 | 84 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 139 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–98
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 59 | 82 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 126 | 59 | inferred_complete_timeline |
| `Action_None` | 128 | 145 | 18 | inferred_complete_timeline |
| `Action_None` | 151 | 181 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_None` | 62 | 72 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 42 | 133 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 139 | 95 | inferred_complete_timeline |
| `Action_None` | 140 | 153 | 14 | inferred_complete_timeline |
| `Action_None` | 158 | 176 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 57 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 88 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 139 | 95 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 139 | 95 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 169 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 98 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 158 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_None` | 112 | 123 | 12 | inferred_complete_timeline |
| `Action_None` | 126 | 199 | 74 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 110 | 69 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_None` | 53 | 105 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 145 | 104 | inferred_complete_timeline |
| `Action_None` | 150 | 177 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 91 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 52 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 54–80 | 27 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 66–71 | 6 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 83–94 | 12 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 87–224 | 57 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 103–219 | 111 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 112–165 | 54 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 112–121 | 10 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 115–141 | 14 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 136–239 | 97 | 5 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 136–139 | 4 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 136–239 | 74 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 157–239 | 83 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 159–239 | 81 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 173–239 | 61 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 175–239 | 59 | 5 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 177–239 | 58 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 203–239 | 28 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `21` (Position_Unknown): Annotated start 42 != Inferred start 66
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=66, end=48. Clamping end to start.
- ⚠️ Action 'Action_None' range [42-51] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-145] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-88] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-72] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-59] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-139] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-176] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-181] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [42-46] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 49, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [49-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-123] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-227] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-223] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>