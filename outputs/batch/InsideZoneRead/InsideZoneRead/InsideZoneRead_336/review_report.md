# Play-Annotation-Generator Annotation Review — InsideZoneRead_336

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_336`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 25 | START | 25 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 28 | START | 38 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 28 | START | 28 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 28 | START | 28 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 28 | START | 28 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 28 | START | 28 | 51 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 37 | END | 25 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `15` | `14` | 43 | START | 43 | 57 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `2` | 43 | START | 43 | 54 |
| ✅ EXACT | `Action_Keep` | QB | `3` | `2` | 55 | START | 55 | 70 |
| ✅ EXACT | `Action_BallCarry` | QB | `3` | `2` | 71 | START | 71 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 90 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 38 | 42 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_Keep` | 55 | 70 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 150 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 66 | 42 | inferred_complete_timeline |
| `Action_None` | 70 | 118 | 49 | inferred_complete_timeline |
| `Action_None` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_None` | 140 | 164 | 25 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 64 | 90 | 27 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 51 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 90 | 32 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 49 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 62 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 36 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 74 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 79 | 55 | inferred_complete_timeline |
| `Action_None` | 85 | 136 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 124 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 48 | 92 | 45 | inferred_complete_timeline |
| `Action_None` | 105 | 180 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 48 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 88 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 87 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–180 | 176 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 30–180 | 149 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–180 | 81 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 68–124 | 53 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 70–180 | 90 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 80–115 | 34 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 93–180 | 85 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 96–111 | 16 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 121–180 | 60 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 133–155 | 23 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 140–179 | 31 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 157–180 | 24 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 171–175 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 672: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [25–37], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [25-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-85] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-66] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-74] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-49] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-62] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-37] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [43-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-173] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-111] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>