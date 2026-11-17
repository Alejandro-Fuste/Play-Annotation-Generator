# Play-Annotation-Generator Annotation Review — Power_327

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_327`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 0
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | LG | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_PullBlock` | RG | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 20 | START | 20 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 20 | START | 20 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 20 | START | 20 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 20 | START | 20 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 20 | START | 20 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 20 | START | 20 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 20 | START | 20 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 20 | START | 20 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 20 | START | 20 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 20 | START | 20 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `16` | 187 | START | 187 | 190 |
| ⚠️ START CHANGED | `Action_DownBlock` | LG | `18` | `18` | 187 | START | 196 | 233 |
| ⚠️ START CHANGED | `Action_PullBlock` | RG | `19` | `19` | 187 | START | 188 | 233 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–318
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 318 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–313
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 310 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 232 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 256 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 297 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 319 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–253
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 253 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 329 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–249
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 233 | 38 | inferred_complete_timeline |
| `Action_None` | 234 | 243 | 10 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 214 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_None` | 234 | 253 | 20 | inferred_complete_timeline |
| `Action_None` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_None` | 277 | 321 | 45 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_PullBlock` | 188 | 233 | 46 | inferred_complete_timeline |
| `Action_None` | 234 | 253 | 20 | inferred_complete_timeline |
| `Action_None` | 255 | 260 | 6 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 185 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 248 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 272 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 329 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 244 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 253 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 282 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 185 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 20–240
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 186 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 222 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 226 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 277 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 251 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 264 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–273
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 273 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–325
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 311 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 325 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 329 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–283
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 283 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 329 | 310 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 20–237 | 207 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 229–329 | 94 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 234–329 | 88 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 254–329 | 71 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 261–329 | 27 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 305–311 | 7 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 310–320 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `18` (LG): Annotated start 187 != Inferred start 196
- ⚠️ `Action_PullBlock` for actor_track_id `19` (RG): Annotated start 187 != Inferred start 188

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 653: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-310] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-297] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-253] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-282] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-311] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-325] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-277] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-318] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-214] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-266] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-279] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-329] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-267] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-273] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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