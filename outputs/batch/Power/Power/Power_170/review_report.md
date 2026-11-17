# Play-Annotation-Generator Annotation Review — Power_170

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_170`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 9 | START | 9 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 9 | START | 9 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 9 | START | 9 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 9 | START | 9 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 9 | START | 9 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 9 | START | 9 | 292 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `1` | `1` | 236 | START | 236 | 273 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `10` | 236 | START | 236 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `2` | `2` | 236 | START | 236 | 253 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 299 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–414
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 325 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 414 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 289 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 419 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 267 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 291 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 315 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 328 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 419 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 235 | 227 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 250 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 307 | 55 | inferred_complete_timeline |
| `Action_None` | 308 | 419 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 235 | 227 | inferred_complete_timeline |
| `Action_PullBlock` | 236 | 253 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 259 | 307 | 49 | inferred_complete_timeline |
| `Action_None` | 308 | 419 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–90
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 65 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 90 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 183 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 419 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–327
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 75 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 242 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 307 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 240 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 256 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 277 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 353 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 365 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 419 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–328
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 221 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 234 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 275 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 328 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 419 | 411 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 66 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 372 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 419 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 9–419 | 376 | 6 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 9–293 | 285 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 271–276 | 6 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 275–304 | 30 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 296–419 | 114 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 297–325 | 29 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 305–419 | 115 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 312–419 | 108 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 340–419 | 68 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 348–419 | 70 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 352–419 | 66 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 398–419 | 16 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 406–417 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 342: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 342: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-273] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [278-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [293-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [236-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-315] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-328] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-289] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-66] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-372] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-325] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-414] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-353] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-365] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [253-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-75] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-242] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-307] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-276] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-304] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-382] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-325] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-353] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-376] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-412] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>