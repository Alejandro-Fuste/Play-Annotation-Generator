# Play-Annotation-Generator Annotation Review — InsideZoneRead_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_46`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `12` | `11` | 172 | START | 172 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 174 | START | 174 | 256 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 174 | START | 175 | 177 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 174 | START | 189 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 174 | START | 174 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 188 | END | 172 | 188 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 197 | START | 197 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `12` | `11` | 203 | START | 203 | 203 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 208 | START | 208 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 223 | START | 223 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–288
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_None` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 197 | 207 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 208 | 222 | 15 | inferred_complete_timeline |
| `Action_None` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_None` | 255 | 273 | 19 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 202 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 171 | 162 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 179 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 203 | 203 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 209 | 256 | 48 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 63 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 244 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 173 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 256 | 83 | inferred_complete_timeline |
| `Action_None` | 257 | 349 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 213 | 42 | inferred_complete_timeline |
| `Action_None` | 217 | 304 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 166 | 148 | inferred_complete_timeline |
| `Action_None` | 172 | 275 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 204 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 222 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 228 | 57 | inferred_complete_timeline |
| `Action_None` | 231 | 271 | 41 | inferred_complete_timeline |
| `Action_None` | 274 | 280 | 7 | inferred_complete_timeline |
| `Action_None` | 284 | 361 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 190 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 37–121 | 85 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 188–322 | 114 | 5 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 202–282 | 70 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 223–416 | 180 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 232–267 | 26 | 4 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 247–479 | 223 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 248–281 | 8 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 250–380 | 111 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 281–367 | 84 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 285–391 | 107 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 291–479 | 189 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 298–343 | 46 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 301–418 | 112 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 302–419 | 118 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 305–479 | 175 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 311–387 | 77 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 311–421 | 111 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 316–479 | 164 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 322–343 | 22 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 328–347 | 20 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 329–387 | 59 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 329–372 | 41 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 336–479 | 144 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 354–479 | 122 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 356–479 | 124 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 388–432 | 43 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 430–477 | 23 | 3 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 468–470 | 3 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 474–479 | 4 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 174 != Inferred start 189
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (5 segments found)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [172–188], lower_priority='Action_ZoneBlock' annotated_start=174, effective_Action_ZoneBlock_start=189.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-304] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-361] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-275] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-39] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [172-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' for track '11' starts at frame 203, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [203-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [205-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-274] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-342] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-416] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-323] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-380] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-367] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-391] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-418] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-387] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-421] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-343] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-347] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-387] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-366] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-479] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-479] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-432] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-440] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-474] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>