# Play-Annotation-Generator Annotation Review — Duo_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_84`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | DE2 | defense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | DT2 | defense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `24` | `20` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 160 |
| ✅ EXACT | `Action_ComboBlock` | DE2 | `12` | `12` | 115 | START | 115 | 177 |
| ✅ EXACT | `Action_ComboBlock` | DT2 | `16` | `16` | 115 | START | 115 | 177 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `18` | `18` | 115 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | `24` | `20` | 115 | START | 169 | 177 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | `18` | `18` | 136 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 270 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 245 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 282 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 298 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 298 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ComboBlock` | 115 | 177 | 63 | inferred_complete_timeline |
| `Action_None` | 178 | 187 | 10 | inferred_complete_timeline |
| `Action_None` | 195 | 204 | 10 | inferred_complete_timeline |
| `Action_None` | 207 | 255 | 49 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 288 | 18 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 201 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 259 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ComboBlock` | 115 | 177 | 63 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_None` | 217 | 234 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 227 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 298 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 222 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 247 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 263 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 16–298 | 283 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 78–298 | 221 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 169–298 | 42 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 174–298 | 125 | 1 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 245–274 | 27 | 3 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 254–293 | 40 | 1 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 276–298 | 21 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `18` (Position_Unknown)
- ⚠️ `Action_ComboBlock` for actor_track_id `24` (Position_Unknown): Annotated start 115 != Inferred start 169
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `18` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '18' has invalid range: start=115, end=37. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '18' has invalid range: start=136, end=37. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-282] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-255] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-201] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-259] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-234] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [169-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-274] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-293] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-287] for track '24' has 3 frames without a visible bounding box.
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

</details>