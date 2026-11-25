# Play-Annotation-Generator Annotation Review — InsideZoneRead_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_141`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 1
- **Action Segments:** 69
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 0
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 9
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `16` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `19` | `16` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LB1 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `16` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 198 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `19` | `16` | 426 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `1` | `0` | 439 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `13` | 439 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `5` | `4` | 439 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `16` | 454 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `19` | `16` | 457 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | LB1 | `13` | `12` | 464 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `19` | `16` | 470 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `22` | `19` | 485 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 519 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 242 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 267 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 204 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 271 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 266 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 295 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 254 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–279 | 280 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–299 | 294 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 22–184 | 38 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 151–177 | 10 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 159–299 | 132 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 165–299 | 95 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 199–299 | 101 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 216–280 | 65 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 226–284 | 59 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 226–263 | 38 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 234–257 | 5 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 240–266 | 13 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 250–263 | 14 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 252–299 | 46 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 253–299 | 44 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 258–285 | 18 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 266–299 | 32 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 267–299 | 28 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | 0 | 128 | 88 | 68.2% | 2–3, 5–12, 14–29, 32–35, 41, 76–77, 109–110, 118–123 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `5` (LT)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `13` (LB1)
- ❌ Missing segment for action `Action_Handoff` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `22` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 10 |
| Other | 12 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 282: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '0' has invalid range: start=439, end=291. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '4' has invalid range: start=439, end=265. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '12' has invalid range: start=464, end=239. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=439, end=267. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=426, end=177. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '16' has invalid range: start=426, end=177. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '16' has invalid range: start=457, end=177. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '16' has invalid range: start=470, end=177. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '19' has invalid range: start=485, end=299. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-266] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-295] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-204] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-254] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-242] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-26] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-269] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Action event 'Action_BallSnap' has invalid start frame 426. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 439. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 439. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 439. Video range is [0, 299].
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 454. Video range is [0, 299].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 457. Video range is [0, 299].
- ⚠️ Action event 'Action_Handoff' has invalid start frame 470. Video range is [0, 299].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 485. Video range is [0, 299].
- ⚠️ Action event 'Action_BlockSecondLevel' has invalid start frame 464. Video range is [0, 299].
- ⚠️ Action event 'Action_None' has invalid start frame 519. Video range is [0, 299].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_141'; source metadata written as null.

</details>