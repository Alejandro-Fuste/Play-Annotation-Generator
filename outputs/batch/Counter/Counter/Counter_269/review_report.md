# Play-Annotation-Generator Annotation Review — Counter_269

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_269`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `23` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `23` | `Group` | 0 | START | 2 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 248 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `20` | `19` | 230 | END | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 241 | START | 241 | 254 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 246 | START | 246 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 249 | START | 249 | 251 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 249 | START | 256 | 286 |
| ✅ EXACT | `Action_PullBlock` | C | `11` | `10` | 249 | START | 249 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `8` | `7` | 249 | START | 249 | 263 |
| ✅ EXACT | `Action_BallCarry` | RB | `23` | `21` | 255 | START | 255 | 273 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 303 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_Handoff` | 241 | 254 | 14 | inferred_complete_timeline |
| `Action_None` | 255 | 419 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 2–273
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 254 | 253 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 273 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 419 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 353 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 407 | 162 | inferred_complete_timeline |
| `Action_None` | 413 | 415 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 249 | 263 | 15 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 267 | 273 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 255 | 10 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_None` | 295 | 302 | 8 | inferred_complete_timeline |
| `Action_None` | 321 | 419 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 245 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 246 | 246 | 1 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 249 | 260 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 286 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 290 | 303 | 14 | inferred_complete_timeline |
| `Action_None` | 304 | 419 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 277 | 303 | 27 | inferred_complete_timeline |
| `Action_None` | 304 | 330 | 27 | inferred_complete_timeline |
| `Action_None` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_None` | 381 | 387 | 7 | inferred_complete_timeline |
| `Action_None` | 394 | 419 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 263 | 18 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 291 | 29 | inferred_complete_timeline |
| `Action_None` | 295 | 419 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 267 | 22 | inferred_complete_timeline |
| `Action_None` | 270 | 283 | 14 | inferred_complete_timeline |
| `Action_None` | 286 | 316 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 304 | 59 | inferred_complete_timeline |
| `Action_None` | 309 | 327 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 367 | 122 | inferred_complete_timeline |
| `Action_None` | 373 | 419 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 419 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 245 | 12 | inferred_complete_timeline |
| `Action_None` | 246 | 340 | 95 | inferred_complete_timeline |
| `Action_None` | 345 | 391 | 47 | inferred_complete_timeline |
| `Action_None` | 402 | 405 | 4 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 343 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_None` | 246 | 414 | 169 | inferred_complete_timeline |
| `Action_None` | 417 | 418 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–409 | 405 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 228–316 | 89 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 249–363 | 114 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 285–371 | 87 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 295–419 | 117 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 312–321 | 10 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 326–419 | 87 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 327–419 | 91 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 332–399 | 56 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 351–419 | 69 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 354–419 | 46 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 380–414 | 30 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 380–419 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `20` (QB)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 540: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '10' has invalid range: start=246, end=230. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=246, end=230. Clamping end to start.
- ⚠️ Action 'Action_None' range [246-343] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-414] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-367] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-353] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-340] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-391] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-405] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [249-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [267-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-395] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-235] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [249-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-407] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-327] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '18' starts at frame 249, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [249-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-330] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [256-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-363] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-371] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-379] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-392] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-414] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-321] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-347] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-373] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-391] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-414] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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