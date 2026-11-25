# Play-Annotation-Generator Annotation Review — InsideZoneRead_338

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_338`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | TE | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB2 | defense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 5 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `19` | 3 | START | 128 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `0` | 6 | START | 6 | 53 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `12` | 6 | START | 6 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `1` | 6 | START | 6 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 6 | START | 6 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 6 | START | 6 | 33 |
| ✅ EXACT | `Action_SnapReceive` | TE | `5` | `4` | 14 | END | 3 | 14 |
| ✅ EXACT | `Action_ReadDefender` | TE | `5` | `4` | 20 | START | 20 | 29 |
| ✅ EXACT | `Action_Keep` | TE | `5` | `4` | 30 | START | 30 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LB2 | `9` | `8` | 31 | START | 31 | 60 |
| ✅ EXACT | `Action_BallCarry` | TE | `5` | `4` | 48 | START | 48 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 163 | 161 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 62 | 60 | inferred_complete_timeline |
| `Action_None` | 68 | 103 | 36 | inferred_complete_timeline |
| `Action_None` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_None` | 135 | 148 | 14 | inferred_complete_timeline |
| `Action_None` | 200 | 207 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_None` | 15 | 19 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 20 | 29 | 10 | inferred_complete_timeline |
| `Action_Keep` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 139 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 54 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 53 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 81 | 25 | inferred_complete_timeline |
| `Action_None` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 81 | 76 | inferred_complete_timeline |
| `Action_None` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_None` | 104 | 132 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 44 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 33 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 57 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 81 | 16 | inferred_complete_timeline |
| `Action_None` | 82 | 91 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 64 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 109 | 107 | inferred_complete_timeline |
| `Action_None` | 118 | 210 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 30 | 28 | inferred_complete_timeline |
| `Action_None` | 70 | 210 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 37 | 35 | inferred_complete_timeline |
| `Action_None` | 44 | 78 | 35 | inferred_complete_timeline |
| `Action_None` | 128 | 167 | 40 | inferred_complete_timeline |
| `Action_None` | 198 | 209 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 84 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 31 | 60 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 106 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 62 | 60 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 120 | 118 | inferred_complete_timeline |
| `Action_None` | 123 | 202 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 60–210 | 150 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 83–125 | 43 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 93–157 | 60 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 128–210 | 83 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 133–210 | 75 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 140–180 | 30 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 146–183 | 38 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 173–181 | 9 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 3 != Inferred start 128
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=128, end=14. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [6-53] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-66] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-74] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-64] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-62] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-103] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [48-139] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-120] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [31-60] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [63-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-167] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-109] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-91] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-62] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-125] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-183] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '28' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_338'; source metadata written as null.

</details>