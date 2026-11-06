# Play-Annotation-Generator Annotation Review — OutsideZoneRead_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_60`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 83
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_Handoff` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 189 | START | 189 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 189 | START | 189 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 189 | START | 189 | 192 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 189 | START | 189 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `6` | 189 | START | 189 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `7` | `7` | 193 | START | 193 | 208 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 198 | START | 198 | 209 |
| ⚠️ START CHANGED | `Action_Handoff` | RB | `7` | `7` | 210 | START | 217 | 220 |

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
- **Visible Frames:** 0–217
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 198 | 209 | 12 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 192 | 66 | inferred_complete_timeline |
| `Action_PressEdge` | 193 | 208 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_PressEdge` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_None` | 229 | 258 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 224 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 247 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 188 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 207 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 208 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 188 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 214 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 254 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 278 | 13 | inferred_complete_timeline |
| `Action_None` | 279 | 314 | 36 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 200 | 12 | inferred_complete_timeline |

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
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 276 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 221 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 250 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 272 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 284 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 289 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 101–230 | 126 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 105–232 | 126 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 108–329 | 203 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 209–329 | 120 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 217–224 | 8 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 222–329 | 107 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 228–329 | 65 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 242–298 | 57 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 256–329 | 71 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 275–329 | 55 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 294–329 | 36 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | 23 | 111 | 15 | 16.9% | 24–34, 36–37, 40–54, 56–76, 80–84, 86–105 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `7` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `7` (RB): Annotated start 210 != Inferred start 217

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-224] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [226-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [233-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [230-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [193-208] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-254] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-314] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-224] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-232] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-321] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-224] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-233] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-298] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-259] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-329] for track '28' has 1 frames without a visible bounding box.
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

</details>