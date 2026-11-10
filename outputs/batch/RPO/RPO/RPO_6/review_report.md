# Play-Annotation-Generator Annotation Review — RPO_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_6`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `25` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 78 | START | 78 | 113 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 78 | START | 78 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 78 | START | 78 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 78 | START | 78 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `7` | 78 | START | 78 | 87 |
| ✅ EXACT | `Action_ReadDefender` | QB | `2` | `2` | 96 | START | 96 | 109 |
| ✅ EXACT | `Action_PullBall` | QB | `2` | `2` | 110 | START | 110 | 130 |
| ✅ EXACT | `Action_ThrowPass` | QB | `2` | `2` | 131 | START | 131 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_ReadDefender` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_PullBall` | 110 | 130 | 21 | inferred_complete_timeline |
| `Action_ThrowPass` | 131 | 141 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 168 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 131 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 162 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_None` | 142 | 174 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 141 | 50 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 113 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 123 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 141 | 50 | inferred_complete_timeline |
| `Action_None` | 142 | 184 | 43 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 140 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_None` | 131 | 194 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 168 | 191 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 106 | 30 | inferred_complete_timeline |
| `Action_None` | 114 | 143 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 122 | 46 | inferred_complete_timeline |
| `Action_None` | 129 | 159 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 104 | 28 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 159 | 47 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 22–147 | 121 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 54–210 | 51 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 139–169 | 30 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 141–183 | 38 | 3 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 157–210 | 45 | 3 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 161–203 | 39 | 3 | Undefined position; Undefined team |
| `21` | `34` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [77-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-159] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-168] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-184] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-106] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '22' has 1 frames without a visible bounding box.
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

</details>