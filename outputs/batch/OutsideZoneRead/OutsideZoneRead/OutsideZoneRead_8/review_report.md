# Play-Annotation-Generator Annotation Review — OutsideZoneRead_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_8`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 62 | START | 62 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 62 | START | 62 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 62 | START | 62 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 62 | START | 62 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 62 | START | 62 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `3` | `3` | 67 | START | 67 | 91 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `4` | `4` | 71 | START | 71 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 86 | START | 86 | 97 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 132 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PressEdge` | 67 | 91 | 25 | inferred_complete_timeline |
| `Action_PressEdge` | 94 | 129 | 36 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 266 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 185 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 139 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 266 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 146 | 85 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 147 | 86 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 147 | 60 | inferred_complete_timeline |
| `Action_None` | 148 | 202 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 147 | 86 | inferred_complete_timeline |
| `Action_None` | 148 | 191 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 9 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 135 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 207 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 174 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 136 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 134 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 184 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 81–177 | 81 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 82–146 | 17 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 108–269 | 155 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 127–200 | 74 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 128–269 | 142 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 134–269 | 136 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 137–199 | 60 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 153–269 | 117 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 157–269 | 97 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 161–269 | 109 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 176–230 | 55 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 239–252 | 13 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [67-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-9] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-207] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-177] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-184] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-252] for track '27' has 1 frames without a visible bounding box.
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

</details>