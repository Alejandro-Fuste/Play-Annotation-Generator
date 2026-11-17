# Play-Annotation-Generator Annotation Review — Power_316

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_316`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 1
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 18 | START | 18 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 18 | START | 18 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 18 | START | 18 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 18 | START | 18 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 18 | START | 43 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `2` | `2` | 190 | START | 190 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `6` | 190 | START | 190 | 220 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `7` | `7` | 190 | START | 190 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `1` | `1` | 190 | START | 190 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–271
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 180 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 208 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 271 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 43–228
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 228 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–238
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_PullBlock` | 190 | 194 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 198 | 209 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 238 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–255
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 166 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 238 | 38 | inferred_complete_timeline |
| `Action_None` | 239 | 255 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–258
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 189 | 172 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 220 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 225 | 238 | 14 | inferred_complete_timeline |
| `Action_None` | 239 | 258 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–258
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 258 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–246
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 246 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–234
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 234 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–329
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 144 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 223 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 288 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 320 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 18–252 | 235 | 3 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 68–253 | 156 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 182–238 | 57 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 185–260 | 9 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 191–203 | 12 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 197–329 | 132 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 213–255 | 43 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 216–285 | 70 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 220–226 | 7 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 228–231 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 247–260 | 14 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 253–322 | 48 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 273–329 | 56 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 276–295 | 14 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 277–320 | 36 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 286–329 | 44 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 304–307 | 4 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 315–329 | 13 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [18-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [190-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [198-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [216-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-175] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-220] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-271] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-320] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>