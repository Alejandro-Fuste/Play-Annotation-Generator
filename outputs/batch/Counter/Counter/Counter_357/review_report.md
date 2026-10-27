# Play-Annotation-Generator Annotation Review — Counter_357

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_357`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_BallCarry` | N/A | N/A | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 192 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 193 | START | 193 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 196 | START | 213 | 244 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `18` | 196 | START | 196 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `21` | `20` | 196 | START | 196 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `17` | `16` | 196 | START | 196 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `1` | `0` | 196 | START | 196 | 263 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 212 | END | 193 | 212 |
| ℹ️ GLOBAL EVENT | `Action_BallCarry` | N/A | N/A | N/A | 236 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 296 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_SnapReceive` | 193 | 212 | 20 | inferred_complete_timeline |
| `Action_None` | 213 | 275 | 63 | inferred_complete_timeline |
| `Action_None` | 277 | 321 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 280 | 88 | inferred_complete_timeline |
| `Action_None` | 286 | 306 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 244 | 52 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 450 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 308 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 226 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 297 | 1 | inferred_complete_timeline |
| `Action_None` | 313 | 361 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 212 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_BallSnap` | 193 | 212 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 244 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 251 | 255 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PullBlock` | 196 | 246 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 256 | 267 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 284 | 296 | 13 | inferred_complete_timeline |
| `Action_None` | 297 | 302 | 6 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 454 | 147 | inferred_complete_timeline |
| `Action_None` | 458 | 479 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 196 | 263 | 68 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 275 | 296 | 22 | inferred_complete_timeline |
| `Action_None` | 297 | 324 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 216 | 24 | inferred_complete_timeline |
| `Action_None` | 221 | 230 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 258 | 66 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 303 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 302 | 110 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 318 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |
| `Action_None` | 272 | 322 | 51 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 259 | 67 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 280 | 88 | inferred_complete_timeline |
| `Action_None` | 283 | 311 | 29 | inferred_complete_timeline |
| `Action_None` | 316 | 320 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 337 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 275 | 83 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 282 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–408
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 278 | 86 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 362 | 31 | inferred_complete_timeline |
| `Action_None` | 369 | 408 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–463
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 463 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 306 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_None` | 193 | 290 | 98 | inferred_complete_timeline |
| `Action_None` | 298 | 306 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–319 | 320 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–261 | 235 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 21–23 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 225–336 | 101 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 254–319 | 65 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 259–294 | 36 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 271–305 | 32 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 290–321 | 31 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 318–326 | 9 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 324–479 | 156 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 330–354 | 25 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 331–333 | 3 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 368–479 | 108 | 2 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 389–400 | 12 | 1 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 404–411 | 5 | 2 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 409–479 | 70 | 2 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 413–479 | 67 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [193–212], lower_priority='Action_DownBlock' annotated_start=196, effective_Action_DownBlock_start=213.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 101 frames exceeds threshold 90 frames [start=196, end=296].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LT) duration 101 frames exceeds threshold 90 frames [start=196, end=296].
- ⚠️ Action 'Action_PullLeadBlock' range [196-263] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-324] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-450] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-259] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-280] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-311] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-337] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-308] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-463] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-306] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [251-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-280] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-306] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-362] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-408] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [196-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [256-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-454] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-302] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-212] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-319] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-226] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [237-240] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 297, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [297-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-361] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-322] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-244] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-325] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-314] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-305] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-354] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-473] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-400] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-458] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>