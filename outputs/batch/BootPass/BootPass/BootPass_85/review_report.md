# Play-Annotation-Generator Annotation Review — BootPass_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_85`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 105 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 106 | START | 106 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `16` | `16` | 114 | START | 114 | 132 |
| ✅ EXACT | `Action_RunBlock` | LT | `20` | `20` | 114 | START | 114 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 114 | START | 114 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `8` | `8` | 114 | START | 114 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `9` | `9` | 114 | START | 122 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 121 | END | 106 | 121 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `14` | `14` | 123 | START | 123 | 144 |
| ✅ EXACT | `Action_BootAway` | QB | `14` | `14` | 145 | START | 145 | 168 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 170 | START | 170 | 178 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 204 | START | 204 | 219 |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 122 | 122 | 1 | inferred_complete_timeline |
| `Action_FakeHandoff` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_BootAway` | 145 | 168 | 24 | inferred_complete_timeline |
| `Action_None` | 169 | 169 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 359 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 124 | 19 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 359 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_SecureCatch` | 204 | 219 | 16 | inferred_complete_timeline |
| `Action_None` | 220 | 257 | 38 | inferred_complete_timeline |
| `Action_None` | 259 | 359 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 359 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 306 | 201 | inferred_complete_timeline |
| `Action_None` | 326 | 350 | 25 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 359 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 132 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 164 | 270 | 107 | inferred_complete_timeline |
| `Action_RunBlock` | 272 | 286 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 290 | 296 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 300 | 359 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 206 | 333 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 155 | 355 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 139 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 326 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 184 | 79 | inferred_complete_timeline |
| `Action_None` | 186 | 359 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 131 | 26 | inferred_complete_timeline |
| `Action_None` | 134 | 215 | 82 | inferred_complete_timeline |
| `Action_None` | 219 | 286 | 68 | inferred_complete_timeline |
| `Action_None` | 290 | 359 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 135 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 137 | 32 | inferred_complete_timeline |
| `Action_None` | 139 | 268 | 130 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 308 | 34 | inferred_complete_timeline |
| `Action_None` | 318 | 359 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 245 | 140 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 291 | 5 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 324 | 23 | inferred_complete_timeline |
| `Action_None` | 327 | 341 | 15 | inferred_complete_timeline |
| `Action_None` | 347 | 356 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 149 | 44 | inferred_complete_timeline |
| `Action_None` | 153 | 230 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 231 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 291 | 186 | inferred_complete_timeline |
| `Action_None` | 293 | 297 | 5 | inferred_complete_timeline |
| `Action_None` | 303 | 314 | 12 | inferred_complete_timeline |
| `Action_None` | 316 | 359 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 359 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 359 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 232 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 135–334 | 199 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 142–342 | 192 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 239–242 | 4 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 251–359 | 109 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 256–359 | 104 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_RunBlock' annotated_start=114, effective_Action_RunBlock_start=122.
- ⚠️ Action 'Action_None' range [106-232] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-359] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-306] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-350] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-286] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [143-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [151-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [206-333] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-324] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-356] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [142-152] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [156-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [164-270] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [272-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [290-296] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [300-359] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-308] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-184] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [142-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [155-355] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-231] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-334] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-359] for track '26' has 1 frames without a visible bounding box.
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