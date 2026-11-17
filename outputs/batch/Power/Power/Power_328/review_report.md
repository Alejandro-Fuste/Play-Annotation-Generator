# Play-Annotation-Generator Annotation Review — Power_328

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_328`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 27 | START | 27 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 27 | START | 27 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 27 | START | 27 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 27 | START | 27 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 27 | START | 27 | 305 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 27 | START | 27 | 225 |
| ✅ EXACT | `Action_DownBlock` | LT | `1` | `1` | 226 | START | 226 | 272 |
| ✅ EXACT | `Action_DownBlock` | LG | `2` | `2` | 226 | START | 226 | 272 |
| ✅ EXACT | `Action_DownBlock` | C | `6` | `6` | 226 | START | 226 | 272 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `4` | 226 | START | 226 | 272 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 27–338
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 297 | 271 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 338 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 225 | 199 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 272 | 47 | inferred_complete_timeline |
| `Action_None` | 273 | 286 | 14 | inferred_complete_timeline |
| `Action_None` | 290 | 306 | 17 | inferred_complete_timeline |
| `Action_None` | 308 | 359 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–318
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 225 | 199 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 272 | 47 | inferred_complete_timeline |
| `Action_None` | 273 | 291 | 19 | inferred_complete_timeline |
| `Action_None` | 293 | 318 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 225 | 199 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 272 | 47 | inferred_complete_timeline |
| `Action_None` | 273 | 300 | 28 | inferred_complete_timeline |
| `Action_None` | 307 | 329 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 225 | 199 | inferred_complete_timeline |
| `Action_PullBlock` | 226 | 272 | 47 | inferred_complete_timeline |
| `Action_None` | 273 | 320 | 48 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 359 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 27–305
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 305 | 279 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 359 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 299 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 27–234
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 234 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 27–347
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 347 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 27–228
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 228 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 27–252 | 226 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 162–229 | 68 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 168–359 | 185 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 185–222 | 38 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 267–359 | 92 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 276–288 | 13 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 281–359 | 69 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 283–359 | 67 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 287–356 | 70 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 295–359 | 48 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 299–359 | 61 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 314–359 | 46 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 38 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [27-311] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-272] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-291] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-338] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-347] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-266] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-222] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-356] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-340] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-342] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-356] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>