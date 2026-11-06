# Play-Annotation-Generator Annotation Review — OutsideZoneRead_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_70`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 93
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
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB1 | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `11` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `4` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `0` | `0` | 111 | START | 111 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 111 | START | 111 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 111 | START | 111 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 111 | START | 111 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 111 | START | 111 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB1 | `4` | `4` | 120 | START | 120 | 142 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `6` | `6` | 120 | START | 120 | 131 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 138 | START | 138 | 144 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 120 | 131 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 222 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PressEdge` | 120 | 142 | 23 | inferred_complete_timeline |
| `Action_PressEdge` | 146 | 166 | 21 | inferred_complete_timeline |
| `Action_None` | 167 | 295 | 129 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 200 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 178 | 68 | inferred_complete_timeline |
| `Action_None` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 142 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 178 | 34 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 110 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 164 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 178 | 68 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 178 | 68 | inferred_complete_timeline |
| `Action_None` | 179 | 300 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 249 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 297 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 262 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 278 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 307 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 148 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 156 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 329 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 176 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 201 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 215 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 278 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 295 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 181–251 | 71 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 193–321 | 129 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 195–329 | 133 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 196–298 | 102 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 211–329 | 115 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 211–329 | 119 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 217–329 | 110 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 219–308 | 90 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 228–329 | 93 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 236–313 | 72 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 265–329 | 65 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 274–288 | 15 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 291–329 | 39 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [179-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [120-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-307] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-200] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-249] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-297] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-134] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-251] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-301] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-308] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-283] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-309] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-288] for track '28' has 2 frames without a visible bounding box.
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