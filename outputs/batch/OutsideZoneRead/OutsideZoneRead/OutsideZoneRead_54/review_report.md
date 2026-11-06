# Play-Annotation-Generator Annotation Review — OutsideZoneRead_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_54`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 7
- **Group Expanded Events:** 7
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 92 |
| ✅ EXACT | `Action_PressEdge` | RB | `5` | `5` | 90 | START | 90 | 108 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 93 | START | 93 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 98 | START | 98 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `14` | 98 | START | 98 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 98 | START | 98 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 98 | START | 98 | 139 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 106 | START | 106 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 93 | 105 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 106 | 118 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 156 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PressEdge` | 90 | 108 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 139 | 42 | inferred_complete_timeline |
| `Action_None` | 140 | 172 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 97 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 139 | 42 | inferred_complete_timeline |
| `Action_None` | 140 | 225 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 139 | 42 | inferred_complete_timeline |
| `Action_None` | 140 | 181 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 139 | 42 | inferred_complete_timeline |
| `Action_None` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 186 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 221 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 193 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–209 | 209 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 35–58 | 19 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 79–126 | 47 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 88–237 | 121 | 5 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 115–346 | 231 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 131–359 | 226 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 145–166 | 21 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 152–311 | 158 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 162–359 | 198 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 176–185 | 10 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 193–359 | 167 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 204–359 | 156 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 207–233 | 26 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 230–242 | 13 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 240–280 | 41 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 263–356 | 85 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 264–323 | 58 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 275–359 | 52 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 290–314 | 25 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 344–346 | 3 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 110: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [90-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [93-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-152] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-198] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-346] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-196] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-237] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-353] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-305] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>