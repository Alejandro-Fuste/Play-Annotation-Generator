# Play-Annotation-Generator Annotation Review — SplitZone_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_238`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 5 | START | 19 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 5 | START | 24 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 5 | START | 6 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 5 | START | 6 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 5 | START | 6 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 5 | START | 6 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 5 | START | 6 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 5 | START | 6 | 168 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `14` | `14` | 166 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 169 | START | 169 | 190 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `14` | 169 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 169 | START | 169 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 169 | START | 169 | 180 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 169 | START | 169 | 189 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 170 | END | 166 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `4` | `4` | 173 | START | 173 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `7` | `7` | 190 | START | 190 | 203 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 196 | START | 196 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 201 | START | 201 | 253 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 296 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–249
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_SnapReceive` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 195 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–319
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 200 | 195 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 253 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 319 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 172 | 167 | inferred_complete_timeline |
| `Action_SplitBlock` | 173 | 199 | 27 | inferred_complete_timeline |
| `Action_SplitBlock` | 202 | 232 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 236 | 296 | 61 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–328
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 168 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 180 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 296 | 115 | inferred_complete_timeline |
| `Action_None` | 297 | 317 | 21 | inferred_complete_timeline |
| `Action_None` | 322 | 328 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 19–307
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 168 | 150 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 190 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 229 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 244 | 262 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 278 | 296 | 19 | inferred_complete_timeline |
| `Action_None` | 297 | 307 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 24–33
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 168 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 189 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 190 | 203 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–295
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 168 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 248 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 295 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–306
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 263 | 90 | inferred_complete_timeline |
| `Action_None` | 294 | 300 | 7 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 6–248
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 248 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–271
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 21 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 165 | 123 | inferred_complete_timeline |
| `Action_None` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 194 | 15 | inferred_complete_timeline |
| `Action_None` | 197 | 224 | 28 | inferred_complete_timeline |
| `Action_None` | 234 | 246 | 13 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 271 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 237 | 72 | inferred_complete_timeline |
| `Action_None` | 242 | 359 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 195 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–258
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 206 | 41 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 235 | 17 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 249 | 7 | inferred_complete_timeline |
| `Action_None` | 251 | 258 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–359
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 166 | 298 | 133 | inferred_complete_timeline |
| `Action_None` | 345 | 359 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 190–306 | 116 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 190–228 | 39 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 225–310 | 36 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 229–283 | 55 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 249–281 | 33 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 255–268 | 14 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 256–288 | 18 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 260–275 | 12 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 284–359 | 76 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 284–359 | 76 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 288–355 | 65 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 316–342 | 27 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 321–323 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 324–334 | 11 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 127 frames exceeds threshold 90 frames [start=169, end=295].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 128 frames exceeds threshold 90 frames [start=169, end=296].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 128 frames exceeds threshold 90 frames [start=169, end=296].
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=166, end=33. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=169, end=33. Clamping end to start.
- ⚠️ Action 'Action_None' range [166-248] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-248] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-253] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-319] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [173-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [202-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-317] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [190-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [206-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [244-262] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-283] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-325] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-355] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-334] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '31' has 1 frames without a visible bounding box.
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

</details>