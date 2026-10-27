# Play-Annotation-Generator Annotation Review — Counter_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_169`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB1 | defense | `6` | `5` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `11` | `Group` | 9 | START | 9 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 9 | START | 9 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `16` | `Group` | 9 | START | 9 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 9 | START | 9 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 9 | START | 9 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 9 | START | 9 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 9 | START | 9 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 9 | START | 9 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 9 | START | 9 | 124 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `12` | `11` | 125 | START | 125 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `12` | `11` | 126 | START | 126 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `15` | `14` | 126 | START | 126 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `17` | 126 | START | 126 | 163 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `21` | `20` | 126 | START | 126 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB1 | `6` | `5` | 126 | START | 126 | 156 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `22` | `21` | 135 | START | 135 | 173 |
| ✅ EXACT | `Action_SnapReceive` | LT | `17` | `16` | 141 | END | 125 | 141 |
| ✅ EXACT | `Action_Handoff` | LT | `17` | `16` | 154 | START | 154 | 173 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `21` | 174 | START | 174 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 214 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 186 | 62 | inferred_complete_timeline |
| `Action_None` | 188 | 479 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 203 | 79 | inferred_complete_timeline |
| `Action_None` | 272 | 298 | 27 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 400 | 93 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 406 | 412 | 7 | inferred_complete_timeline |
| `Action_None` | 415 | 479 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 206 | 82 | inferred_complete_timeline |
| `Action_None` | 212 | 240 | 29 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 424 | 171 | inferred_complete_timeline |
| `Action_None` | 427 | 479 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–189
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 125 | 117 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 189 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 229 | 105 | inferred_complete_timeline |
| `Action_None` | 232 | 241 | 10 | inferred_complete_timeline |
| `Action_None` | 255 | 477 | 223 | inferred_complete_timeline |
| `Action_None` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_None` | 142 | 153 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 154 | 173 | 20 | inferred_complete_timeline |
| `Action_None` | 174 | 479 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–168
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 168 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–167
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 125 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 163 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 125 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 147 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 214 | 63 | inferred_complete_timeline |
| `Action_None` | 215 | 479 | 265 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 165 | 41 | inferred_complete_timeline |
| `Action_None` | 167 | 479 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–290
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 290 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–227
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 197 | 73 | inferred_complete_timeline |
| `Action_None` | 203 | 227 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 125 | 117 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 126 | 156 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 158 | 214 | 57 | inferred_complete_timeline |
| `Action_None` | 215 | 479 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 217 | 93 | inferred_complete_timeline |
| `Action_None` | 228 | 479 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 232 | 108 | inferred_complete_timeline |
| `Action_None` | 239 | 439 | 201 | inferred_complete_timeline |
| `Action_None` | 442 | 479 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 165 | 41 | inferred_complete_timeline |
| `Action_None` | 169 | 479 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 430 | 306 | inferred_complete_timeline |
| `Action_None` | 434 | 442 | 9 | inferred_complete_timeline |
| `Action_None` | 444 | 479 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 187 | 63 | inferred_complete_timeline |
| `Action_None` | 189 | 479 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 124 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 479 | 355 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 9–479 | 470 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 9–256 | 243 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 9–479 | 471 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 12–21 | 8 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 172–203 | 22 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 181–479 | 299 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 186–388 | 203 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 212–479 | 267 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 214–479 | 255 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 252–479 | 228 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 289–479 | 182 | 3 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 300–479 | 110 | 16 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 385–386 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 387–404 | 9 | 3 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 405–406 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 443–444 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 463–479 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 340: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [125-174] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-232] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-439] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-187] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-479] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [126-156] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-430] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-477] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-479] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-203] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-400] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-479] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-147] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-424] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [166-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-217] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-168] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-21] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-479] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-388] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-432] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-423] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-309] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-375] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-399] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-432] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-441] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-479] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-469] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>