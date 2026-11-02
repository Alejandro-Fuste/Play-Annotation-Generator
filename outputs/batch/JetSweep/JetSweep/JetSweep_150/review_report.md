# Play-Annotation-Generator Annotation Review — JetSweep_150

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_150`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `15` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 2 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 50 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `15` | 41 | START | 107 | 107 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `13` | `12` | 44 | START | 44 | 73 |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | `1` | `0` | 51 | START | 51 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 51 | START | 51 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 51 | START | 51 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 51 | START | 51 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 51 | START | 51 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 51 | START | 51 | 120 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 60 | END | 41 | 60 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 64 | START | 64 | 73 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `13` | `12` | 74 | START | 75 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `2` | `1` | 88 | START | 88 | 95 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_Toss` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 145 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–56
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_None` | 41 | 56 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 87 | 37 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 101 | 115 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 120 | 70 | inferred_complete_timeline |
| `Action_None` | 121 | 150 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 118 | 68 | inferred_complete_timeline |
| `Action_None` | 122 | 144 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 86 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_None` | 121 | 139 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 120 | 70 | inferred_complete_timeline |
| `Action_None` | 121 | 139 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 105 | 65 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 210 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 81 | 41 | inferred_complete_timeline |
| `Action_None` | 84 | 142 | 59 | inferred_complete_timeline |
| `Action_None` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_None` | 168 | 175 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 33–130 | 16 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 44–106 | 62 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 52–209 | 154 | 2 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 69–134 | 66 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 107–145 | 37 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 111–143 | 31 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 111–114 | 4 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 115–120 | 6 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 131–176 | 46 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 140–210 | 71 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 147–210 | 64 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 167–171 | 5 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 182–210 | 26 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 41 != Inferred start 107
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `13` (Position_Unknown): Annotated start 74 != Inferred start 75
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=107, end=60. Clamping end to start.
- ⚠️ Action 'Action_None' range [121-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [88-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [101-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-165] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [44-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [75-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>