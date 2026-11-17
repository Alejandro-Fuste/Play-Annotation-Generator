# Play-Annotation-Generator Annotation Review — Power_276

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_276`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 13 | START | 13 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 13 | START | 13 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 13 | START | 13 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 13 | START | 13 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 13 | START | 55 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 13 | START | 13 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 13 | START | 13 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF | `14` | `14` | 127 | START | 127 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `3` | `3` | 127 | START | 127 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `6` | 127 | START | 127 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `12` | `12` | 127 | START | 127 | 214 |

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
- **Visible Frames:** 13–271
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 167 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 271 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 55–75
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 55 | 67 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 75 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 166 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 220 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–189
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 167 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 189 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–279
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 191 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 279 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 13–225
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 146 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 197 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 225 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–323
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 214 | 88 | inferred_complete_timeline |
| `Action_PullBlock` | 221 | 229 | 9 | inferred_complete_timeline |
| `Action_None` | 230 | 304 | 75 | inferred_complete_timeline |
| `Action_None` | 307 | 319 | 13 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 203 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 329 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 30–203
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 203 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–246
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 202 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 246 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 27–188
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 107 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 188 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–329
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 203 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 274 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 289 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–253
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 248 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 253 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–329
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 168 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 310 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–209
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 209 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 13–329 | 304 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 13–326 | 310 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 13–329 | 291 | 9 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 126–273 | 94 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 149–228 | 73 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 166–208 | 43 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 174–329 | 154 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 184–206 | 23 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 190–327 | 136 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 208–329 | 115 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 222–293 | 66 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 263–329 | 65 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 263–280 | 18 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 552: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (DT1) duration 103 frames exceeds threshold 90 frames [start=127, end=229].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=127, end=229].
- ⚠️ Action 'Action_PreSnap' range [13-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-227] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-203] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-326] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [184-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-176] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-228] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-258] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-310] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-279] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-214] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-44] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-188] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-163] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-228] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-211] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-302] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-327] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-299] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-224] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-267] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-329] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-267] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-293] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-275] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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