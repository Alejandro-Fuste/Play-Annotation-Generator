# Play-Annotation-Generator Annotation Review — WRSlowScreens_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ReleaseToScreen` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `31` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 8 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `19` | `16` | 6 | START | 45 | 45 |
| ✅ EXACT | `Action_PassBlock` | RG | `12` | `12` | 9 | START | 9 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 9 | START | 9 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 9 | START | 9 | 68 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `5` | 9 | START | 9 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `6` | `6` | 9 | START | 9 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 19 | END | 6 | 19 |
| ✅ EXACT | `Action_ReleaseToScreen` | RT | `5` | `5` | 38 | START | 38 | 210 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `11` | `11` | 70 | START | 70 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | `31` | `24` | 98 | START | 98 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 19 | 14 | inferred_complete_timeline |
| `Action_None` | 20 | 69 | 50 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 143 | 65 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_None` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 68 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 111 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 51 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 111 | 103 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 126 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 197 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 37 | 29 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 65 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 115 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 58 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 74 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 112 | 107 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 45–49 | 5 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 56–203 | 141 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 72–210 | 139 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 81–210 | 128 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 87–91 | 5 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 91–210 | 120 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 95–102 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 96–210 | 109 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 98–156 | 58 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 103–210 | 108 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 104–210 | 83 | 4 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 146–152 | 7 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 173–210 | 16 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 178–210 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (Position_Unknown): Annotated start 6 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `31` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=45, end=19. Clamping end to start.
- ⚠️ Action 'Action_None' range [6-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [38-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-197] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [199-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-22] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-51] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-161] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [98-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [105-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>