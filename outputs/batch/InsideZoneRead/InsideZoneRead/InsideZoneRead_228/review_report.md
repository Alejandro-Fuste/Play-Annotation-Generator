# Play-Annotation-Generator Annotation Review — InsideZoneRead_228

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_228`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 7 | START | 7 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 7 | START | 7 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 7 | START | 23 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 7 | START | 23 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 7 | START | 7 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 7 | START | 58 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 7 | START | 7 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `13` | 85 | START | 85 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 88 | START | 111 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 88 | START | 88 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `16` | 88 | START | 88 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 88 | START | 88 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `18` | 88 | START | 88 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 101 | END | 85 | 101 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `10` | 103 | START | 103 | 115 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 116 | START | 116 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 123 | START | 123 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–207
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_None` | 102 | 102 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 207 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–205
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 122 | 116 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 205 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 87 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 158 | 71 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–210
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 87 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 103 | 16 | inferred_complete_timeline |
| `Action_None` | 164 | 210 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–202
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 46 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 95 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 202 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 23–163
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 87 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 117 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 141 | 22 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 58–210
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 158 | 36 | inferred_complete_timeline |
| `Action_None` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 7–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 85 | 207 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 85 | 126 | 42 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–135
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 85 | 135 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–184
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 38 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 84 | 44 | inferred_complete_timeline |
| `Action_None` | 85 | 152 | 68 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 41 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 84 | 41 | inferred_complete_timeline |
| `Action_None` | 85 | 175 | 91 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 85 | 177 | 93 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 7–15 | 9 | 1 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 7–26 | 20 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 7–35 | 29 | 1 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 7–18 | 12 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 7–38 | 32 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 42–54 | 13 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 137–210 | 74 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [85–101], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=102.
- ⚠️ Action 'Action_PreSnap' range [7-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-26] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-41] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-175] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [116-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-38] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [85-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [99-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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