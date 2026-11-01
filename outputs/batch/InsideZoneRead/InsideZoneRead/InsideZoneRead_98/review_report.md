# Play-Annotation-Generator Annotation Review — InsideZoneRead_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_98`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 166 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `14` | `13` | 165 | START | 166 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 167 | START | 167 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `10` | 167 | START | 167 | 183 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 167 | START | 179 | 256 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 167 | START | 167 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 167 | START | 167 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 178 | END | 165 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `6` | `5` | 182 | START | 182 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `6` | `5` | 196 | START | 196 | 202 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 207 | START | 207 | 215 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_SnapReceive` | 165 | 178 | 14 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 270 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 215 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–191
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 166 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 183 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 191 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 233 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 166–299
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 256 | 78 | inferred_complete_timeline |
| `Action_None` | 257 | 272 | 16 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 202 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 237 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 247 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 243 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 223 | 59 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 260 | 18 | inferred_complete_timeline |
| `Action_None` | 263 | 290 | 28 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 249 | 85 | inferred_complete_timeline |
| `Action_None` | 251 | 299 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 226 | 62 | inferred_complete_timeline |
| `Action_None` | 228 | 271 | 44 | inferred_complete_timeline |
| `Action_None` | 277 | 299 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 211 | 47 | inferred_complete_timeline |
| `Action_None` | 214 | 266 | 53 | inferred_complete_timeline |
| `Action_None` | 269 | 299 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 42–205
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 164 | 123 | inferred_complete_timeline |
| `Action_None` | 165 | 205 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_None` | 165 | 204 | 40 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 57–65 | 5 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 201–299 | 87 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 207–246 | 18 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 211–299 | 69 | 4 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 225–238 | 14 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 240–299 | 60 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 242–278 | 35 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 256–280 | 25 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 265–299 | 31 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 283–299 | 16 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `14` (C): Annotated start 165 != Inferred start 166
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 167 != Inferred start 179
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [166–178], lower_priority='Action_ZoneBlock' annotated_start=167, effective_Action_ZoneBlock_start=179.
- ⚠️ Action 'Action_None' range [165-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [182-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [196-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-270] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-290] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-237] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [243-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-243] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [245-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [166-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-259] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-278] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-297] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>