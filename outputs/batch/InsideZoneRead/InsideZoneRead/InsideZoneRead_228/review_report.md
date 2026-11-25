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
- **Action Segments:** 73
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `24` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `18` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `28` | `22` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `28` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `28` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 7 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 7 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 23 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 23 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 7 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 58 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 7 | 128 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `24` | `19` | 95 | START | 137 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 98 | START | 99 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 98 | START | 98 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `16` | 98 | START | 98 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 98 | START | 98 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `18` | 98 | START | 98 | 100 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `28` | `22` | 105 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `28` | `22` | 109 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `16` | `15` | 116 | START | 116 | 117 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `28` | `22` | 122 | START | 165 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 132 | START | 170 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 7 | 94 | 88 | inferred_complete_timeline |
| `Action_None` | 95 | 122 | 28 | inferred_complete_timeline |
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
| `Action_PreSnap` | 7 | 128 | 122 | inferred_complete_timeline |
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
| `Action_PreSnap` | 7 | 97 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 162 | 65 | inferred_complete_timeline |
| `Action_None` | 163 | 167 | 5 | inferred_complete_timeline |
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
| `Action_PreSnap` | 23 | 97 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 103 | 6 | inferred_complete_timeline |
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
| `Action_PreSnap` | 76 | 95 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 162 | 4 | inferred_complete_timeline |
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
| `Action_PreSnap` | 23 | 97 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 120 | 141 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 162 | 162 | 1 | inferred_complete_timeline |
| `Action_None` | 163 | 163 | 1 | inferred_complete_timeline |

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
| `Action_PreSnap` | 81 | 97 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 162 | 40 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

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
| `Action_PreSnap` | 7 | 94 | 88 | inferred_complete_timeline |
| `Action_None` | 95 | 207 | 113 | inferred_complete_timeline |

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
| `Action_PreSnap` | 7 | 94 | 88 | inferred_complete_timeline |
| `Action_None` | 95 | 126 | 32 | inferred_complete_timeline |
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
| `Action_PreSnap` | 7 | 94 | 88 | inferred_complete_timeline |
| `Action_None` | 95 | 135 | 41 | inferred_complete_timeline |

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
| `Action_PreSnap` | 41 | 94 | 54 | inferred_complete_timeline |
| `Action_None` | 95 | 152 | 58 | inferred_complete_timeline |
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
| `Action_PreSnap` | 44 | 94 | 51 | inferred_complete_timeline |
| `Action_None` | 95 | 175 | 81 | inferred_complete_timeline |
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
| `Action_PreSnap` | 7 | 94 | 88 | inferred_complete_timeline |
| `Action_None` | 95 | 177 | 83 | inferred_complete_timeline |
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
| `19` | `24` | Position_Unknown | Team_Unknown | 137–210 | 74 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 165–210 | 46 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `24` (Position_Unknown): Annotated start 95 != Inferred start 137
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `22` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `22` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (3 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `28` (Position_Unknown): Annotated start 122 != Inferred start 165
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=137, end=105. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '22' has invalid range: start=165, end=105. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '22' has invalid range: start=165, end=121. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '22' has invalid range: start=165, end=131. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [7-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-26] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-41] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-175] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-38] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-38] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [116-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [120-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 163, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [163-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '22' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_228'; source metadata written as null.

</details>