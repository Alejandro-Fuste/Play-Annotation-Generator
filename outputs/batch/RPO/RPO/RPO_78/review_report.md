# Play-Annotation-Generator Annotation Review — RPO_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 75
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `26` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_RunBlock` | LT | `1` | `1` | 81 | START | 81 | 139 |
| ✅ EXACT | `Action_RunBlock` | C | `14` | `14` | 81 | START | 81 | 139 |
| ✅ EXACT | `Action_RunBlock` | RG | `3` | `3` | 81 | START | 81 | 139 |
| ✅ EXACT | `Action_RunBlock` | RT | `5` | `5` | 81 | START | 81 | 139 |
| ✅ EXACT | `Action_RunBlock` | LG | `9` | `9` | 81 | START | 81 | 139 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 88 | START | 88 | 97 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 98 | START | 98 | 109 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 133 | START | 133 | 139 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_ThrowPass` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 160 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 107 | 28 | inferred_complete_timeline |
| `Action_None` | 113 | 169 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 122 | 43 | inferred_complete_timeline |
| `Action_None` | 126 | 155 | 30 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 163 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 192 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_None` | 150 | 166 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 192 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 139 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 163 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 171 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 168 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 238 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 180 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 103 | 24 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 213 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 91–155 | 16 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 116–199 | 81 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 135–149 | 15 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 135–146 | 12 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 146–201 | 46 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 156–239 | 84 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 157–196 | 40 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 221–232 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 84 | 85 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 43 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [80-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-238] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-171] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-168] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-92] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-199] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '28' has 1 frames without a visible bounding box.
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