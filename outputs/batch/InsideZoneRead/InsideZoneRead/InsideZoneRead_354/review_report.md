# Play-Annotation-Generator Annotation Review — InsideZoneRead_354

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_354`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 85
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 16 | START | 16 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 19 | START | 19 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 19 | START | 19 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 19 | START | 19 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 19 | START | 19 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 19 | START | 31 | 57 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 30 | END | 16 | 30 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 33 | START | 33 | 38 |
| ✅ EXACT | `Action_Keep` | QB | `13` | `12` | 39 | START | 39 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 70 | START | 70 | 152 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 92 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 33 | 38 | 6 | inferred_complete_timeline |
| `Action_Keep` | 39 | 69 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 152 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 182 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 80 | 65 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 100 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_None` | 52 | 104 | 53 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 91 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 92 | 74 | inferred_complete_timeline |
| `Action_None` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 57 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 80 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 85 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 81 | 66 | inferred_complete_timeline |
| `Action_None` | 87 | 95 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 142 | 127 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 200 | 185 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 78 | 63 | inferred_complete_timeline |
| `Action_None` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 132 | 158 | 27 | inferred_complete_timeline |
| `Action_None` | 162 | 171 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 23–109 | 50 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 61–210 | 137 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 81–87 | 7 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 101–174 | 71 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 104–193 | 73 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 159–208 | 50 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 190–193 | 4 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (6 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_ZoneBlock' annotated_start=19, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [16-50] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-80] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-85] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-57] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-158] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-60] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-68] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-174] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
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

</details>