# Play-Annotation-Generator Annotation Review — OutsideZoneRead_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_26`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 90 | START | 90 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `13` | 90 | START | 90 | 124 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `14` | `14` | 90 | START | 92 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `2` | 90 | START | 90 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 90 | START | 90 | 139 |
| ✅ EXACT | `Action_PressEdge` | RB | `9` | `9` | 92 | START | 92 | 121 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `5` | 95 | START | 95 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `5` | 116 | START | 116 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PressEdge` | 92 | 121 | 30 | inferred_complete_timeline |
| `Action_None` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_None` | 151 | 223 | 73 | inferred_complete_timeline |
| `Action_None` | 235 | 244 | 10 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 329 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 139 | 50 | inferred_complete_timeline |
| `Action_None` | 140 | 171 | 32 | inferred_complete_timeline |
| `Action_None` | 175 | 253 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 135 | 46 | inferred_complete_timeline |
| `Action_None` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 189 | 292 | 104 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 182 | 36 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 213 | 23 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 124 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 134 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 208 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 206 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 311 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

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
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 291 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 312 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 322 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 106–188 | 83 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 116–329 | 170 | 4 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 120–198 | 76 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 127–136 | 10 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 139–304 | 156 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 140–199 | 60 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 157–169 | 13 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 171–280 | 100 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 174–241 | 64 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 175–329 | 155 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 183–329 | 127 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 195–319 | 106 | 3 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 204–233 | 30 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 206–329 | 117 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 219–329 | 105 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 234–292 | 58 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 247–299 | 49 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 253–329 | 77 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 259–329 | 68 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 296–329 | 26 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (LG): Annotated start 90 != Inferred start 92
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-312] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-125] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-171] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-253] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [116-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [119-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-206] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-311] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [92-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-135] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-280] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-241] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-329] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-315] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-270] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-315] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-286] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-288] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-299] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-292] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-308] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-321] for track '37' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>