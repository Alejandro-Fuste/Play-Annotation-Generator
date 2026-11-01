# Play-Annotation-Generator Annotation Review — InsideZoneRead_191

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_191`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 2
- **Action Segments:** 80
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 17 | START | 17 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 20 | START | 20 | 43 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 20 | START | 20 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 20 | START | 20 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 20 | START | 20 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 20 | START | 31 | 35 |
| ✅ EXACT | `Action_SnapReceive` | RB | `11` | `10` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ReadDefender` | RB | `11` | `10` | 33 | START | 33 | 50 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `12` | `11` | 45 | START | 45 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | RB | `11` | `10` | 51 | START | 51 | 56 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 64 | START | 64 | 71 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 71 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 33 | 50 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 180 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 99 | 80 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 126 | 27 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 44 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 45 | 99 | 55 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 72 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 50 | 34 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 180 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 112 | 96 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 112 | 96 | inferred_complete_timeline |
| `Action_None` | 114 | 180 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 19–52 | 33 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 44–152 | 109 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 56–180 | 55 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 62–63 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 64–156 | 87 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 71–180 | 99 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 80–180 | 95 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 96–180 | 85 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 100–180 | 81 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 102–180 | 79 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 107–180 | 60 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 160–162 | 3 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | 0 | 16 | 17 | 100.0% | None |
| `15` | `16` | 41 | 47 | 3 | 42.9% | 42–45 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_ZoneBlock' range [20-43] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-71] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-43] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-112] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-50] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [51-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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