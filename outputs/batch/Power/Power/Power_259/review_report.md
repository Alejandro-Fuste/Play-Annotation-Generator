# Play-Annotation-Generator Annotation Review — Power_259

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_259`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 10 | START | 10 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 10 | START | 10 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 10 | START | 10 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `18` | `Group` | 10 | START | 10 | 387 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 10 | START | 10 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 10 | START | 10 | 351 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 10 | START | 10 | 217 |
| ✅ EXACT | `Action_DownBlock` | RB | `14` | `14` | 218 | START | 218 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `19` | 218 | START | 218 | 242 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `22` | 218 | START | 218 | 254 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 217 | 208 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 254 | 37 | inferred_complete_timeline |
| `Action_None` | 255 | 276 | 22 | inferred_complete_timeline |
| `Action_None` | 280 | 389 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 387 | 378 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 351 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 389 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 217 | 208 | inferred_complete_timeline |
| `Action_PullBlock` | 218 | 254 | 37 | inferred_complete_timeline |
| `Action_None` | 255 | 375 | 121 | inferred_complete_timeline |
| `Action_None` | 377 | 389 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 217 | 208 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 242 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 254 | 1 | inferred_complete_timeline |
| `Action_None` | 255 | 359 | 105 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–253
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 246 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 253 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 287 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 246 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 389 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 311 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 357 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 369 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–319
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 306 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 319 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 283 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 389 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 389 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 283 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 10–389 | 372 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 10–389 | 380 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 10–389 | 379 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 10–45 | 36 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 10–389 | 380 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 47–187 | 87 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 275–389 | 115 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 287–312 | 4 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 301–389 | 61 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 345–389 | 16 | 5 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 370–389 | 10 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 517: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 518: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [10-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-351] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-369] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-357] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-287] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-276] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-16] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-306] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-319] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-387] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 255, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [255-359] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-351] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [218-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 255, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [255-375] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-98] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-139] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-308] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-335] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-356] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-370] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-380] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-373] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>