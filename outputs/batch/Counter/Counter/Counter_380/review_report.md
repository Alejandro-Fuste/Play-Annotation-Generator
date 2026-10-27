# Play-Annotation-Generator Annotation Review — Counter_380

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_380`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 108
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
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | WR | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 49 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `17` | 47 | START | 56 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `15` | `14` | 50 | START | 50 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `7` | `6` | 50 | START | 50 | 73 |
| ✅ EXACT | `Action_PullBlock` | WR | `4` | `3` | 50 | START | 50 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `9` | `8` | 50 | START | 50 | 86 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `13` | `12` | 64 | END | 47 | 64 |
| ✅ EXACT | `Action_Handoff` | DE2 | `13` | `12` | 77 | START | 77 | 95 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `6` | `5` | 96 | START | 136 | 169 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 169 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 134 | 85 | inferred_complete_timeline |
| `Action_None` | 135 | 210 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 165 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 73 | 27 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_None` | 131 | 159 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_None` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 91 | 104 | 14 | inferred_complete_timeline |
| `Action_None` | 106 | 139 | 34 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 50 | 86 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 98 | 120 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 124 | 132 | 9 | inferred_complete_timeline |
| `Action_None` | 137 | 169 | 33 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_None` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_None` | 96 | 144 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 116 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 206 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 60 | 14 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_None` | 55 | 81 | 27 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 210 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 127 | 81 | inferred_complete_timeline |
| `Action_None` | 132 | 144 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–38 | 39 | 1 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–78 | 79 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–152 | 148 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 46–63 | 15 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 56–124 | 58 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 75–100 | 10 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 87–113 | 25 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 93–125 | 33 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 94–149 | 50 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 97–127 | 27 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 103–108 | 6 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 121–167 | 44 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 127–144 | 18 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 140–146 | 7 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 144–210 | 43 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 147–163 | 17 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 47 != Inferred start 56
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (4 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `6` (RB): Annotated start 96 != Inferred start 136

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 762: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 762: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-78] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-122] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-165] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [89-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [98-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [124-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-206] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-66] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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