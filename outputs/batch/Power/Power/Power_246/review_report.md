# Play-Annotation-Generator Annotation Review — Power_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_246`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB4 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 3 | START | 3 | 264 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 3 | START | 3 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 3 | START | 3 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 3 | START | 3 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 3 | START | 3 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 3 | START | 3 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 3 | START | 3 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `3` | `3` | 218 | START | 218 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB4 | `5` | `5` | 218 | START | 218 | 225 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–129
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 129 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 275 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 294 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 327 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–245
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 238 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–289
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 256 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 273 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 277 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 289 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–300
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 264 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 294 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 300 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–245
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 234 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 245 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–287
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 217 | 215 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 238 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–294
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 282 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 294 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 259 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 269 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 312 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 349 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 355 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 240 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 294 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 359 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–306
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 306 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–263
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 263 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 359 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–279
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 252 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 269 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 217 | 215 | inferred_complete_timeline |
| `Action_PullBlock` | 218 | 225 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 237 | 273 | 37 | inferred_complete_timeline |
| `Action_None` | 274 | 301 | 28 | inferred_complete_timeline |
| `Action_None` | 304 | 359 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–133
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 133 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 113–120 | 5 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 244–311 | 68 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 248–358 | 102 | 5 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 250–280 | 31 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 253–337 | 85 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 261–359 | 98 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 262–307 | 44 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 311–359 | 48 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 320–347 | 26 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 323–349 | 10 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 325–359 | 35 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 334–359 | 26 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 345–359 | 15 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 494: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 494: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 494: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 494: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-263] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-252] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-238] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-312] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [218-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [228-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-282] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-294] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-294] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-311] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-275] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-297] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-313] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-320] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-358] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-337] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-285] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-307] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-322] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-349] for track '25' has 3 frames without a visible bounding box.
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