# Play-Annotation-Generator Annotation Review — Power_248

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_248`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 0
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB5 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB5 | `10` | `10` | 216 | START | 216 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RB | `7` | `7` | 216 | START | 216 | 224 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 83 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 194 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 226 | 270 | 45 | inferred_complete_timeline |
| `Action_None` | 271 | 307 | 37 | inferred_complete_timeline |
| `Action_None` | 323 | 334 | 12 | inferred_complete_timeline |
| `Action_None` | 339 | 384 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 246 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 419 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 281 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 288 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 312 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 387 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 419 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 220 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 239 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 274 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 170 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 238 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 319 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 70–213
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 133 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 213 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 261 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 390 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 135 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 154 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 215 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 231 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 270 | 32 | inferred_complete_timeline |
| `Action_None` | 271 | 385 | 115 | inferred_complete_timeline |
| `Action_None` | 387 | 406 | 20 | inferred_complete_timeline |
| `Action_None` | 412 | 419 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–418 | 414 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–326 | 324 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–241 | 231 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 9–46 | 38 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 31–64 | 34 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 140–419 | 278 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 202–295 | 71 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 220–362 | 118 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 220–419 | 198 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 224–240 | 17 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 227–419 | 180 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 252–419 | 168 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 268–300 | 31 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 290–419 | 130 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 294–418 | 117 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 365–411 | 42 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 369–419 | 51 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 374–419 | 46 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 397–418 | 22 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 404–419 | 12 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 414–418 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 498: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 498: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 498: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 498: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 498: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 498: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-386] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-407] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-415] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-387] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-303] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-83] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-255] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-317] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-326] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-194] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [216-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-334] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-238] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-154] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-161] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-385] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-406] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-295] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-353] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-315] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-240] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-300] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-388] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-418] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-404] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-411] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-418] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-407] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-419] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-418] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>