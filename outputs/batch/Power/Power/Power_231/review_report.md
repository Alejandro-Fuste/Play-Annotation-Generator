# Play-Annotation-Generator Annotation Review — Power_231

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_231`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 54
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 7 | START | 7 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 7 | START | 7 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 7 | START | 7 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 7 | START | 7 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 7 | START | 7 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 7 | START | 7 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 7 | START | 7 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 7 | START | 7 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 7 | START | 7 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 7 | START | 7 | 214 |
| ✅ EXACT | `Action_DownBlock` | QB | `11` | `11` | 183 | START | 183 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `16` | 183 | START | 183 | 191 |
| ✅ EXACT | `Action_DownBlock` | RT | `20` | `20` | 183 | START | 183 | 238 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `21` | 183 | START | 183 | 238 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–275
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 182 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 238 | 56 | inferred_complete_timeline |
| `Action_None` | 239 | 275 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–340
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 205 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 340 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 139 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 359 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 214 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–355
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 355 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 182 | 176 | inferred_complete_timeline |
| `Action_PullBlock` | 183 | 238 | 56 | inferred_complete_timeline |
| `Action_None` | 239 | 248 | 10 | inferred_complete_timeline |
| `Action_None` | 256 | 326 | 71 | inferred_complete_timeline |
| `Action_None` | 329 | 337 | 9 | inferred_complete_timeline |
| `Action_None` | 340 | 359 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 182 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 191 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 238 | 38 | inferred_complete_timeline |
| `Action_None` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 182 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 238 | 56 | inferred_complete_timeline |
| `Action_None` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–237
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 237 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 337 | 331 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 359 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 235 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 359 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–355
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 244 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 335 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 355 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 271 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 359 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 341 | 335 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 326 | 320 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 7–359 | 353 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 235–359 | 125 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 269–359 | 87 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 342–348 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 464: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-235] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-341] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-355] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-326] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-335] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-355] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-337] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-337] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>