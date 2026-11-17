# Play-Annotation-Generator Annotation Review — Power_315

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_315`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `28` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 316 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 62 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 281 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `17` | 230 | START | 237 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `28` | `25` | 230 | START | 236 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `18` | 230 | START | 235 | 251 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 288 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 359 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 316 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 350 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 62–270
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 99 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 218 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 268 | 270 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 123–290
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 203 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 290 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 121–244
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 244 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 170 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 121–359
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 246 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 359 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 324 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 294 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 315 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 327 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 312 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 250 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 277 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 359 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–57 | 58 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–55 | 14 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 4–9 | 6 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 109–359 | 177 | 11 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 127–136 | 5 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 234–359 | 124 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 236–250 | 12 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 241–359 | 80 | 8 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 257–305 | 33 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 267–359 | 93 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 302–305 | 4 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 309–354 | 44 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 326–354 | 24 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 330–359 | 25 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 335–359 | 25 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `28` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 115 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-350] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-356] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-359] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-250] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-277] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-324] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-315] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-312] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-316] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-129] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [237-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [262-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [268-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-144] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [235-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [253-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-170] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-359] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-318] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-245] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [249-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-305] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-359] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-277] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-334] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-354] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-343] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-335] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-349] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>