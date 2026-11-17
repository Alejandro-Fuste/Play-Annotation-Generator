# Play-Annotation-Generator Annotation Review — Power_353

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_353`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 20 | START | 20 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 20 | START | 20 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 20 | START | 20 | 305 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 20 | START | 20 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 20 | START | 20 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 20 | START | 20 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 20 | START | 63 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 20 | START | 20 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `16` | 250 | START | 250 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `21` | 250 | START | 250 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `18` | `18` | 250 | START | 250 | 269 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–305
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 305 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–355
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 289 | 270 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 341 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 355 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 359 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 249 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 303 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 359 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 20–304
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 29 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 249 | 218 | inferred_complete_timeline |
| `Action_PullBlock` | 250 | 269 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 283 | 293 | 11 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 63–288
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 63 | 249 | 187 | inferred_complete_timeline |
| `Action_DownBlock` | 250 | 250 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 271 | 282 | 12 | inferred_complete_timeline |
| `Action_None` | 283 | 288 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–335
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 56 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 246 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 335 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–293
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 286 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 359 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–332
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 257 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 332 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 278 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 308 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 359 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–343
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 343 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 359 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 286 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 284 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 359 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–352
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 352 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–332
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 313 | 294 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 332 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 20–288 | 269 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 20–251 | 231 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 20–293 | 273 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 20–314 | 285 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 286–359 | 73 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 305–359 | 46 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 320–359 | 39 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 322–359 | 38 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 339–359 | 17 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 349–359 | 4 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 353–359 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 705: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 706: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-359] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-257] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-332] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-332] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-289] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-341] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-355] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-286] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [250-261] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [267-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-314] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-305] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [250-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-303] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-335] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '21' starts at frame 250, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [250-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [256-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [262-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-301] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-336] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-351] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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