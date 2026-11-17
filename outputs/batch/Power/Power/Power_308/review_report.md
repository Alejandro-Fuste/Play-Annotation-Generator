# Play-Annotation-Generator Annotation Review — Power_308

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_308`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 12 | START | 12 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 12 | START | 12 | 362 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 12 | START | 12 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 12 | START | 12 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 12 | START | 12 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 12 | START | 12 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 12 | START | 12 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 12 | START | 12 | 285 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 156 | START | 156 | 174 |
| ✅ EXACT | `Action_DownBlock` | LT | `8` | `8` | 156 | START | 156 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `12` | 156 | START | 156 | 226 |

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
- **Visible Frames:** 12–371
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 285 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 345 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 371 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 389 | 378 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–323
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 180 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 323 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 242 | 87 | inferred_complete_timeline |
| `Action_None` | 243 | 389 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 362 | 351 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–284
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 174 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 242 | 66 | inferred_complete_timeline |
| `Action_None` | 243 | 272 | 30 | inferred_complete_timeline |
| `Action_None` | 274 | 281 | 8 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–378
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 156 | 226 | 71 | inferred_complete_timeline |
| `Action_PullBlock` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_None` | 243 | 265 | 23 | inferred_complete_timeline |
| `Action_None` | 275 | 332 | 58 | inferred_complete_timeline |
| `Action_None` | 337 | 378 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 213 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 389 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–302
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 260 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 302 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–360
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 354 | 343 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 360 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–312
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 164 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 312 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 162 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–227
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 207 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 227 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 190 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 389 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 12–389 | 362 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 36–389 | 347 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 167–320 | 152 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 190–238 | 49 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 227–344 | 118 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 231–247 | 17 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 252–338 | 87 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 266–389 | 98 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 287–389 | 103 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 299–368 | 54 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 320–359 | 40 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 333–389 | 55 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 339–382 | 33 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 349–389 | 20 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 350–373 | 23 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 362–389 | 28 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 368–374 | 7 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [12-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-320] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-302] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-354] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-360] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-345] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-371] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-312] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-362] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [156-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-332] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-272] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-378] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-316] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-344] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-338] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-312] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-334] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-345] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-364] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-389] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-366] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-361] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-370] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-389] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-373] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-374] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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