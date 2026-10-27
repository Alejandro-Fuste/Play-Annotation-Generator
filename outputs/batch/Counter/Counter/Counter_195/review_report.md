# Play-Annotation-Generator Annotation Review — Counter_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_195`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | defense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | LB2 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 127 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 128 | START | 128 | 130 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `16` | `15` | 131 | START | 131 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `2` | `1` | 131 | START | 131 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 131 | START | 131 | 181 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `20` | 131 | START | 131 | 209 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `14` | `13` | 131 | START | 131 | 219 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB2 | `4` | `3` | 137 | START | 137 | 174 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `12` | `11` | 141 | END | 128 | 141 |
| ✅ EXACT | `Action_Handoff` | DE2 | `12` | `11` | 160 | START | 160 | 174 |
| ✅ EXACT | `Action_BallCarry` | LB2 | `4` | `3` | 175 | START | 175 | 278 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 219 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 196 | 69 | inferred_complete_timeline |
| `Action_None` | 259 | 281 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 228 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 131 | 219 | 89 | inferred_complete_timeline |
| `Action_None` | 220 | 289 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 219 | 73 | inferred_complete_timeline |
| `Action_None` | 220 | 278 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 279 | 152 | inferred_complete_timeline |
| `Action_None` | 283 | 320 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 244 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 329 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 200 | 73 | inferred_complete_timeline |
| `Action_None` | 204 | 252 | 49 | inferred_complete_timeline |
| `Action_None` | 256 | 329 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SnapReceive` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_None` | 175 | 274 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 219 | 89 | inferred_complete_timeline |
| `Action_None` | 220 | 274 | 55 | inferred_complete_timeline |
| `Action_None` | 281 | 294 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 291 | 164 | inferred_complete_timeline |
| `Action_None` | 295 | 310 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 204 | 77 | inferred_complete_timeline |
| `Action_None` | 206 | 213 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 278 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 152 | 25 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 276 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 329 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–299 | 297 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–249 | 250 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–186 | 185 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–226 | 208 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–309 | 305 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 195–329 | 133 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 198–280 | 83 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 210–329 | 119 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 251–304 | 31 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 317–324 | 8 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 49 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [128-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-278] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-228] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-249] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-181] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [131-209] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-309] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-324] for track '27' has 1 frames without a visible bounding box.
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