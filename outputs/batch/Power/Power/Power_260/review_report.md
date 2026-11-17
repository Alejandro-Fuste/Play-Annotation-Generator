# Play-Annotation-Generator Annotation Review — Power_260

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_260`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 9 | START | 9 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 9 | START | 9 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 9 | START | 114 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 9 | START | 9 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 9 | START | 9 | 308 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 9 | START | 9 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 9 | START | 9 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `12` | `12` | 223 | START | 223 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 223 | START | 223 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `5` | `5` | 223 | START | 223 | 240 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–360
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 308 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 318 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 339 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 360 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 287 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 401 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 289 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 419 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 222 | 214 | inferred_complete_timeline |
| `Action_PullBlock` | 223 | 240 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 251 | 268 | 18 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |
| `Action_None` | 273 | 419 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 114–315
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 114 | 222 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 236 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 240 | 268 | 29 | inferred_complete_timeline |
| `Action_None` | 269 | 291 | 23 | inferred_complete_timeline |
| `Action_None` | 303 | 312 | 10 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–249
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 249 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 222 | 214 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 234 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 259 | 268 | 10 | inferred_complete_timeline |
| `Action_None` | 269 | 419 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 326 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 419 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 228 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 270 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 267 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 335 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 419 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–340
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 340 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–258
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 258 | 250 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 9–374 | 355 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 9–289 | 281 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 9–53 | 43 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 223–392 | 152 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 234–305 | 51 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 240–419 | 162 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 246–414 | 143 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 274–311 | 38 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 284–288 | 5 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 289–354 | 60 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 297–342 | 41 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 325–419 | 94 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 334–386 | 53 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 338–351 | 12 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 341–367 | 24 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 346–419 | 74 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 348–419 | 69 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 368–419 | 52 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 394–419 | 22 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 520: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-340] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-374] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-401] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-339] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-360] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [223-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 269, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [269-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-335] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [223-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-34] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-228] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [223-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-360] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-367] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-386] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-392] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-305] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-326] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-336] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-410] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-311] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-354] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-385] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-386] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-347] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-367] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-396] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-419] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-412] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>