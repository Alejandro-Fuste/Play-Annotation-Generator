# Play-Annotation-Generator Annotation Review — Power_270

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_270`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 29
- **Ball Tracks:** 2
- **Action Segments:** 47
- **Validation Warnings:** 65
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
- **Inferred Coverage Segments (Action_None):** 32
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 30 | START | 30 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 30 | START | 30 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 30 | START | 30 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 30 | START | 30 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 30 | START | 30 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 30 | START | 30 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 30 | START | 30 | 293 |
| ✅ EXACT | `Action_DownBlock` | LT | `11` | `11` | 239 | START | 239 | 302 |
| ✅ EXACT | `Action_DownBlock` | C | `2` | `2` | 239 | START | 239 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `7` | `7` | 239 | START | 239 | 256 |

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
- **Visible Frames:** 30–389
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 268 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 366 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 383 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 30–293
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 293 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 30–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 238 | 209 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 302 | 64 | inferred_complete_timeline |
| `Action_None` | 303 | 389 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 30–389
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 256 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 389 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 30–333
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 238 | 209 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 302 | 64 | inferred_complete_timeline |
| `Action_None` | 303 | 333 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 30–331
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 331 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 30–389
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 238 | 209 | inferred_complete_timeline |
| `Action_PullBlock` | 239 | 256 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 264 | 302 | 39 | inferred_complete_timeline |
| `Action_None` | 303 | 389 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 30–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 389 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 30–322
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 322 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 200–389
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 200 | 389 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 30–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 389 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 30–304
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 304 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 30–116
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 116 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 30–341 | 312 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 30–389 | 360 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 152–173 | 11 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 166–302 | 137 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 235–255 | 21 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 278–389 | 104 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 285–361 | 77 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 358–389 | 32 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 364–380 | 16 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 378–385 | 7 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 379–389 | 11 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | 251 | 257 | 7 | 100.0% | None |
| `20` | `21` | 257 | 259 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 540: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [30-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-366] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-383] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [239-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [259-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [264-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-389] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-331] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-302] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-361] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-376] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-380] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-381] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-385] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>