# Play-Annotation-Generator Annotation Review — OutsideZoneRead_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_104`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 71
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 125 | START | 125 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 128 | START | 128 | 163 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 128 | START | 128 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 128 | START | 141 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 128 | START | 128 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 128 | START | 128 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 140 | END | 125 | 140 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `4` | 147 | START | 147 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `5` | `4` | 150 | START | 150 | 160 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 168 | START | 168 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_Keep` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_Keep` | 162 | 167 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 299 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 205 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 212 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 146 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 193 | 43 | inferred_complete_timeline |
| `Action_None` | 194 | 253 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 193 | 66 | inferred_complete_timeline |
| `Action_None` | 194 | 236 | 43 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_BallSnap` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 193 | 53 | inferred_complete_timeline |
| `Action_None` | 194 | 232 | 39 | inferred_complete_timeline |
| `Action_None` | 234 | 260 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 163 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 193 | 23 | inferred_complete_timeline |
| `Action_None` | 194 | 276 | 83 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 193 | 66 | inferred_complete_timeline |
| `Action_None` | 194 | 194 | 1 | inferred_complete_timeline |
| `Action_None` | 196 | 260 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 181 | 57 | inferred_complete_timeline |
| `Action_None` | 183 | 226 | 44 | inferred_complete_timeline |
| `Action_None` | 228 | 263 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 208 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 200 | 76 | inferred_complete_timeline |
| `Action_None` | 203 | 299 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 226 | 102 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 269 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_None` | 125 | 235 | 111 | inferred_complete_timeline |
| `Action_None` | 237 | 258 | 22 | inferred_complete_timeline |
| `Action_None` | 260 | 276 | 17 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 161–168 | 8 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 229–299 | 71 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 254–299 | 40 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 258–299 | 36 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 262–268 | 7 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 292–299 | 7 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 70 | 94 | 24 | 96.0% | 91 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [125–140], lower_priority='Action_ZoneBlock' annotated_start=128, effective_Action_ZoneBlock_start=141.
- ⚠️ Action 'Action_None' range [125-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [150-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-193] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 194, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [194-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-212] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-258] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-276] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-181] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '24' has 1 frames without a visible bounding box.
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