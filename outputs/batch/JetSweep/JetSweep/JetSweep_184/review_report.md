# Play-Annotation-Generator Annotation Review — JetSweep_184

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_184`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `13` | `12` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `13` | `12` | 24 | START | 24 | 51 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `10` | `9` | 25 | START | 25 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | `4` | `3` | 26 | START | 26 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 26 | START | 26 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 26 | START | 26 | 43 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `4` | `3` | 26 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 26 | START | 26 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 34 | END | 25 | 34 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 48 | START | 48 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `13` | `12` | 52 | START | 52 | 55 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_None` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_Toss` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 134 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 73 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 43 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 61 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 76 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 49 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 119 | 46 | inferred_complete_timeline |
| `Action_None` | 120 | 150 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 73 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 119 | 27 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LeadBlock` | 26 | 44 | 19 | inferred_complete_timeline |
| `Action_LeadBlock` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 57 | 105 | 49 | inferred_complete_timeline |
| `Action_None` | 120 | 132 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_None` | 37 | 77 | 41 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 137 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_None` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_None` | 57 | 81 | 25 | inferred_complete_timeline |
| `Action_None` | 83 | 146 | 64 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_None` | 74 | 114 | 41 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 115 | 91 | inferred_complete_timeline |
| `Action_None` | 125 | 146 | 22 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 67 | 43 | inferred_complete_timeline |
| `Action_None` | 71 | 100 | 30 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 122 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_None` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 183 | 64 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 24–168 | 141 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 32–74 | 29 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 33–160 | 105 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 37–152 | 97 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 37–48 | 12 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 39–210 | 168 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 59–194 | 132 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 65–114 | 50 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 74–182 | 101 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 80–110 | 31 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 81–168 | 88 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 104–210 | 105 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 118–144 | 27 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 128–210 | 76 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 128–180 | 53 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 141–171 | 31 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 145–149 | 5 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 153–210 | 54 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 154–210 | 44 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
- ⚠️ Overlapping action conflict at frame 26 for track '3': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '3' (RT) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 94 frames exceeds threshold 90 frames [start=26, end=119].
- ⚠️ Action 'Action_None' range [25-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-49] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [26-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [51-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [57-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-134] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-77] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-81] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-146] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-142] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-112] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-70] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-114] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-173] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-174] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>