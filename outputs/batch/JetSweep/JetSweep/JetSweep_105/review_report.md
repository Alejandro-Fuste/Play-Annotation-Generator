# Play-Annotation-Generator Annotation Review — JetSweep_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_105`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 23 | START | 23 | 75 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `19` | 49 | START | 70 | 70 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 53 | START | 53 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 53 | START | 53 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 53 | START | 53 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 53 | START | 53 | 53 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 53 | START | 53 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 61 | END | 49 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 68 | START | 68 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `5` | `4` | 76 | START | 77 | 84 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `12` | `11` | 77 | START | 77 | 146 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_Toss` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_None` | 76 | 118 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_LeadBlock` | 53 | 77 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_JetMotion` | 23 | 75 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 198 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 97 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 71 | 23 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 103 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 76 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 77 | 146 | 70 | inferred_complete_timeline |
| `Action_None` | 147 | 173 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 17 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 58 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 62 | 100 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 83 | 35 | inferred_complete_timeline |
| `Action_None` | 87 | 239 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 82 | 34 | inferred_complete_timeline |
| `Action_None` | 84 | 106 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 146 | 98 | inferred_complete_timeline |
| `Action_None` | 148 | 158 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 130 | 82 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 93 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 108 | 60 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 203 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 137 | 89 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 61–239 | 162 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 70–113 | 44 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 88–177 | 86 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 99–107 | 9 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 114–238 | 115 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–215 | 93 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 128–205 | 78 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 179–239 | 59 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 198–239 | 42 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 199–233 | 15 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 49 != Inferred start 70
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
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
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=70, end=61. Clamping end to start.
- ⚠️ Action 'Action_None' range [49-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-203] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [23-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-198] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [53-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-82] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-17] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-52] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '17' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [53-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-113] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-215] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-205] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '29' has 1 frames without a visible bounding box.
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