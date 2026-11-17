# Play-Annotation-Generator Annotation Review — Power_230

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_230`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 1
- **Action Segments:** 111
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_DownBlock` | LB1 | defense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 12 | START | 12 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 12 | START | 12 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 12 | START | 12 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 12 | START | 12 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 12 | START | 12 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 12 | START | 12 | 171 |
| ✅ EXACT | `Action_DownBlock` | TE | `1` | `1` | 205 | START | 205 | 241 |
| ✅ EXACT | `Action_DownBlock` | LB1 | `12` | `12` | 205 | START | 205 | 241 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `21` | `19` | 205 | START | 205 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `4` | 205 | START | 205 | 219 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–266
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 33 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 255 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 266 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–176
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 171 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–283
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 204 | 95 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 241 | 37 | inferred_complete_timeline |
| `Action_None` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_None` | 251 | 261 | 11 | inferred_complete_timeline |
| `Action_None` | 263 | 283 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–397
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 73 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 169 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 277 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 397 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 204 | 193 | inferred_complete_timeline |
| `Action_PullBlock` | 205 | 219 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 234 | 241 | 8 | inferred_complete_timeline |
| `Action_None` | 242 | 419 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–286
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 97 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 286 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–263
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 258 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 263 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–353
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 199 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 279 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 286 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 341 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 349 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 353 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–283
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 243 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 264 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 283 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–279
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 95 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 182 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 262 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 279 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 204 | 193 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 241 | 37 | inferred_complete_timeline |
| `Action_None` | 242 | 419 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–278
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 250 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 278 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–287
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 242 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 287 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–283
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 99 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 230 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 283 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–143
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 143 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 12–109 | 98 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 12–128 | 97 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 154–157 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 190–419 | 207 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 212–419 | 197 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 229–354 | 121 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 230–266 | 37 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 267–419 | 150 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 284–419 | 132 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 287–419 | 132 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 305–342 | 20 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 316–419 | 104 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 316–418 | 101 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 317–419 | 103 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 328–419 | 92 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 330–419 | 90 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 332–419 | 88 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 333–338 | 6 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 344–419 | 76 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 352–396 | 44 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 355–361 | 7 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 355–419 | 65 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 356–361 | 6 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 359–419 | 61 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 367–381 | 12 | 2 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 414–415 | 2 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 132 | 195 | 38 | 59.4% | 139–150, 152, 155–161, 165–166, 170–173 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 462: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 462: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [12-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-279] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-95] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-261] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-283] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-258] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-397] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [205-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [223-227] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-97] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-199] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-279] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-341] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-349] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-255] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-230] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-283] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-59] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-139] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-40] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [205-234] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-393] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-257] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-390] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-354] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-282] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-380] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-321] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-411] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-418] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-338] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-358] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-396] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-361] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-419] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-372] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-381] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>