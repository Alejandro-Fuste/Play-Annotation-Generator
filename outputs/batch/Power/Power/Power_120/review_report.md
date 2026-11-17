# Play-Annotation-Generator Annotation Review — Power_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_120`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 100
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 24 | START | 24 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 24 | START | 24 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 24 | START | 24 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 24 | START | 24 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 24 | START | 33 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 24 | START | 24 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 24 | START | 24 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 24 | START | 24 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `12` | 204 | START | 204 | 207 |
| ✅ EXACT | `Action_DownBlock` | RG | `2` | `2` | 204 | START | 204 | 284 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `20` | `19` | 204 | START | 270 | 313 |

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
- **Visible Frames:** 24–321
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 228 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 262 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 321 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 33–241
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 230 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 241 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–212
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 170 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 212 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–212
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 208 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 212 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–222
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 203 | 180 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 217 | 222 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–389
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 210 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 244 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 389 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 24–284
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 203 | 180 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 284 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 24–389
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 216 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 258 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 283 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 389 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–370
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 248 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 301 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 363 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 370 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–300
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 300 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 290 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 355 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 24–385
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 355 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 385 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–361
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 361 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 272 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 343 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 389 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 330 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 389 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 222–308 | 67 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 226–267 | 6 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 246–320 | 75 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 254–389 | 136 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 270–318 | 49 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 275–389 | 115 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 279–330 | 52 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 285–382 | 98 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 293–389 | 97 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 294–389 | 96 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 298–389 | 92 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 308–389 | 82 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 312–389 | 76 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 313–389 | 77 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 319–389 | 71 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 323–354 | 18 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 335–369 | 31 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 368–371 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `20` (Position_Unknown): Annotated start 204 != Inferred start 270

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [24-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-330] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-272] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-301] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-363] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-370] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-355] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-385] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-389] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-355] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-389] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-228] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-262] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [217-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-258] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-230] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-241] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-235] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-308] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-320] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [270-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-330] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-382] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-374] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-349] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-369] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-371] for track '34' has 1 frames without a visible bounding box.
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