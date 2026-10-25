# Play-Annotation-Generator Annotation Review — BootPass_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_101`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | LB2 | defense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 195 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 188 | START | 188 | 196 |
| ✅ EXACT | `Action_RunBlock` | LG | `11` | `11` | 196 | START | 196 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 196 | START | 197 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 196 | START | 196 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `2` | `2` | 196 | START | 196 | 240 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 196 | START | 196 | 244 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 196 | END | 188 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `1` | `1` | 220 | START | 220 | 229 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `6` | `6` | 234 | START | 234 | 279 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `1` | `1` | 235 | START | 235 | 285 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | LB2 | `5` | `5` | 249 | START | 249 | 262 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `1` | `1` | 294 | START | 294 | 306 |

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
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_SnapReceive` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 255 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 349 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 240 | 53 | inferred_complete_timeline |
| `Action_None` | 243 | 247 | 5 | inferred_complete_timeline |
| `Action_None` | 251 | 318 | 68 | inferred_complete_timeline |
| `Action_None` | 324 | 364 | 41 | inferred_complete_timeline |
| `Action_None` | 367 | 373 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 240 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 248 | 309 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 317 | 318 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 217 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_BallSnap` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 197 | 222 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 307 | 320 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 324 | 351 | 28 | inferred_complete_timeline |
| `Action_RunBlock` | 364 | 389 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 244 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 289 | 337 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 339 | 389 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 227 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 264 | 355 | 92 | inferred_complete_timeline |
| `Action_RunBlock` | 366 | 389 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 244 | 57 | inferred_complete_timeline |
| `Action_None` | 246 | 389 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 232 | 45 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 227 | 40 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 369 | 182 | inferred_complete_timeline |
| `Action_None` | 376 | 385 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_SecureCatch` | 266 | 318 | 53 | inferred_complete_timeline |
| `Action_SecureCatch` | 321 | 358 | 38 | inferred_complete_timeline |
| `Action_None` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 378 | 191 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–389 | 388 | 7 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–389 | 386 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 236–255 | 16 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 257–314 | 23 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 259–276 | 17 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 293–389 | 88 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 302–389 | 88 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 319–355 | 18 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 329–353 | 13 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 336–348 | 5 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 340–370 | 31 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 355–389 | 29 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 365–389 | 16 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 374–389 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 182: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [188–196], lower_priority='Action_RunBlock' annotated_start=196, effective_Action_RunBlock_start=197.
- ⚠️ Action 'Action_None' range [188-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [220-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [248-309] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [317-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-378] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [249-262] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [266-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [321-358] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-374] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-385] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [197-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [248-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [254-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [257-258] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [307-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [324-351] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-240] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-318] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-364] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-373] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [264-355] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-244] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [248-255] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [285-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [289-337] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [339-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-314] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-370] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-387] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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