# Play-Annotation-Generator Annotation Review — Counter_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_20`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 229 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 172 | START | 172 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 182 | START | 182 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 182 | START | 188 | 192 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 182 | START | 182 | 240 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `6` | `5` | 182 | START | 182 | 217 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 187 | END | 172 | 187 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 199 | START | 199 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 230 | START | 230 | 232 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 259 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 171 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 187 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 199 | 229 | 31 | inferred_complete_timeline |
| `Action_None` | 230 | 331 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 376 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 379 | 384 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 182 | 217 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 240 | 69 | inferred_complete_timeline |
| `Action_None` | 244 | 337 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 219 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_None` | 260 | 331 | 72 | inferred_complete_timeline |
| `Action_None` | 369 | 389 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 187 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 208 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 210 | 259 | 50 | inferred_complete_timeline |
| `Action_None` | 260 | 303 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PullBlock` | 182 | 240 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 282 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 228 | 57 | inferred_complete_timeline |
| `Action_None` | 250 | 389 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 171 | 72 | inferred_complete_timeline |
| `Action_None` | 172 | 182 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 267 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 254 | 83 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 232 | 61 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 318 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 378 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 236–299 | 64 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 256–358 | 102 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 271–379 | 88 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 276–389 | 114 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 285–294 | 10 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 319–389 | 71 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 339–389 | 51 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 358–389 | 32 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 363–378 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [172–187], lower_priority='Action_DownBlock' annotated_start=182, effective_Action_DownBlock_start=188.
- ⚠️ Action 'Action_None' range [172-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-337] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-254] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-318] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-376] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [379-384] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-282] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-259] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-331] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-240] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-331] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [188-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-378] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-353] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-378] for track '27' has 1 frames without a visible bounding box.
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