# Play-Annotation-Generator Annotation Review — Dagger_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_3`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BreakInside` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 180 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 181 | START | 181 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 184 | START | 184 | 306 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 184 | START | 184 | 301 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 184 | START | 184 | 243 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `2` | 184 | START | 184 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `7` | `7` | 184 | START | 186 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 185 | END | 181 | 185 |
| ✅ EXACT | `Action_BreakInside` | WR3 | `0` | `0` | 199 | START | 199 | 311 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `1` | `1` | 199 | START | 199 | 272 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 263 | START | 263 | 272 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_SnapReceive` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 186 | 262 | 77 | inferred_complete_timeline |
| `Action_ThrowPass` | 263 | 272 | 10 | inferred_complete_timeline |
| `Action_None` | 273 | 340 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 264 | 84 | inferred_complete_timeline |
| `Action_None` | 280 | 316 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_ClearToEdge` | 199 | 272 | 74 | inferred_complete_timeline |
| `Action_None` | 273 | 331 | 59 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 271 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_BreakInside` | 199 | 311 | 113 | inferred_complete_timeline |
| `Action_None` | 312 | 340 | 29 | inferred_complete_timeline |
| `Action_None` | 342 | 345 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 286 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 238 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 306 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_BallSnap` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 195 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 212 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 301 | 118 | inferred_complete_timeline |
| `Action_PassBlock` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 243 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 254 | 260 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 290 | 359 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 346 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 359 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 355 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 359 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 355 | 175 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 256 | 76 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 271 | 348 | 78 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 319 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 359 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 344 | 164 | inferred_complete_timeline |
| `Action_None` | 353 | 358 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 244 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_None` | 181 | 359 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 194–202 | 8 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 203–215 | 12 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 228–232 | 5 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 233–273 | 30 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 242–274 | 13 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 262–357 | 71 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 280–292 | 5 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 288–359 | 68 | 3 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 312–348 | 27 | 3 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 318–359 | 40 | 3 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 325–352 | 28 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 349–355 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [181–185], lower_priority='Action_PassBlock' annotated_start=184, effective_Action_PassBlock_start=186.
- ⚠️ Action 'Action_None' range [312-340] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-331] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-359] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-355] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-212] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-346] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-264] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-316] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-348] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [310-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-301] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [303-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-355] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-344] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-358] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [247-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [251-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [254-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-340] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-264] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-320] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-348] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-331] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-355] for track '37' has 1 frames without a visible bounding box.
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

</details>