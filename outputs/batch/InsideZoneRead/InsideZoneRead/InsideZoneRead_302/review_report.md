# Play-Annotation-Generator Annotation Review — InsideZoneRead_302

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_302`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 23 | START | 23 | 37 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 26 | START | 38 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 26 | START | 26 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 26 | START | 26 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 26 | START | 26 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 26 | START | 26 | 57 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 37 | END | 23 | 37 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 42 | START | 42 | 42 |
| ✅ EXACT | `Action_Keep` | QB | `5` | `4` | 43 | START | 43 | 65 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 66 | START | 66 | 183 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 93 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_Keep` | 43 | 65 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 183 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 143 | 49 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 62 | 40 | inferred_complete_timeline |
| `Action_None` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_None` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 114 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 93 | 42 | inferred_complete_timeline |
| `Action_None` | 94 | 112 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 93 | 56 | inferred_complete_timeline |
| `Action_None` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 57 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 93 | 35 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 78 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 69 | 14 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 210 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 36 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 117 | 58 | inferred_complete_timeline |
| `Action_None` | 124 | 156 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 153 | 18 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 144 | 122 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 93 | 71 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 78 | 56 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 75–114 | 39 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 78–210 | 125 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 82–210 | 116 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 84–96 | 13 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 92–168 | 74 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 96–159 | 60 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 102–210 | 108 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 117–210 | 88 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 121–210 | 76 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 129–210 | 79 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 137–210 | 70 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 143–210 | 58 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 166–210 | 36 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 167–202 | 35 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 182–202 | 20 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 195–203 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 26 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [23–37], lower_priority='Action_ZoneBlock' annotated_start=26, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [23-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-183] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-78] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-144] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-69] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-153] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-143] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-117] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-177] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-195] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '32' has 1 frames without a visible bounding box.
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