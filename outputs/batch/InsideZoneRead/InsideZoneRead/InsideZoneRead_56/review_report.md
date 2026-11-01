# Play-Annotation-Generator Annotation Review — InsideZoneRead_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_56`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 8 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `11` | `10` | 131 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `0` | 133 | START | 133 | 171 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `1` | 133 | START | 133 | 201 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 133 | START | 133 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 133 | START | 133 | 231 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 141 | END | 131 | 141 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 145 | START | 145 | 158 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 159 | START | 159 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 167 | START | 169 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 130 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 141 | 11 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 145 | 158 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 159 | 166 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 199 | 33 | inferred_complete_timeline |
| `Action_None` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 204 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 216 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 132 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 171 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 201 | 69 | inferred_complete_timeline |
| `Action_None` | 278 | 290 | 13 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 231 | 99 | inferred_complete_timeline |
| `Action_None` | 232 | 267 | 36 | inferred_complete_timeline |
| `Action_None` | 270 | 283 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 294 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 169 | 39 | inferred_complete_timeline |
| `Action_None` | 171 | 204 | 34 | inferred_complete_timeline |
| `Action_None` | 208 | 223 | 16 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 241 | 111 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 259 | 11 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 6–144 | 20 | 3 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 41–60 | 20 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 139–299 | 154 | 3 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 140–299 | 132 | 8 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 149–295 | 130 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 153–299 | 134 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 154–299 | 89 | 10 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 183–258 | 75 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 195–299 | 71 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 203–299 | 93 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 223–265 | 43 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 245–283 | 28 | 6 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 279–280 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 289–296 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `11` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 99 frames exceeds threshold 90 frames [start=133, end=231].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 99 frames exceeds threshold 90 frames [start=133, end=231].
- ⚠️ Segment 'Action_BallSnap' for track '10' has invalid range: start=131, end=60. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-171] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-294] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-267] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-19] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-60] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-170] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-257] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-258] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-291] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>