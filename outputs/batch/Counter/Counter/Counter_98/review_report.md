# Play-Annotation-Generator Annotation Review — Counter_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_98`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 182 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 183 | START | 183 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `1` | 192 | START | 192 | 248 |
| ✅ EXACT | `Action_DownBlock` | RG | `3` | `2` | 192 | START | 192 | 268 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | `6` | `5` | 192 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LG | `6` | `5` | 192 | START | 192 | 268 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `10` | `9` | 192 | START | 192 | 258 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 194 | END | 183 | 194 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 218 | START | 218 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_SnapReceive` | 183 | 194 | 12 | inferred_complete_timeline |
| `Action_None` | 195 | 217 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 389 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 257 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 270 | 88 | inferred_complete_timeline |
| `Action_None` | 275 | 338 | 64 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 192 | 258 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_PullBlock` | 192 | 268 | 77 | inferred_complete_timeline |
| `Action_None` | 269 | 371 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_BallSnap` | 183 | 194 | 12 | inferred_complete_timeline |
| `Action_None` | 195 | 242 | 48 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 268 | 77 | inferred_complete_timeline |
| `Action_None` | 269 | 389 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 248 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 250 | 268 | 19 | inferred_complete_timeline |
| `Action_None` | 269 | 282 | 14 | inferred_complete_timeline |
| `Action_None` | 284 | 345 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 312 | 130 | inferred_complete_timeline |
| `Action_None` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 334 | 152 | inferred_complete_timeline |
| `Action_None` | 336 | 379 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_None` | 204 | 233 | 30 | inferred_complete_timeline |
| `Action_None` | 242 | 295 | 54 | inferred_complete_timeline |
| `Action_None` | 303 | 339 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 243 | 61 | inferred_complete_timeline |
| `Action_None` | 246 | 263 | 18 | inferred_complete_timeline |
| `Action_None` | 268 | 288 | 21 | inferred_complete_timeline |
| `Action_None` | 305 | 308 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 202 | 20 | inferred_complete_timeline |
| `Action_None` | 204 | 389 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 30–57 | 23 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 95–389 | 215 | 9 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 167–389 | 221 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 239–250 | 11 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 255–389 | 135 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 263–270 | 8 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 315–321 | 7 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 318–389 | 72 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 320–359 | 19 | 4 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 327–373 | 23 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 337–389 | 15 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 340–342 | 3 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `6` (LG)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Overlapping action conflict at frame 192 for track '5': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Action 'Action_DownBlock' range [192-248] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-312] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-371] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-338] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [192-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-379] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-233] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-339] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-242] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-34] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-344] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '29' has 1 frames without a visible bounding box.
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

</details>