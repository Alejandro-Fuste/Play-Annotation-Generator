# Play-Annotation-Generator Annotation Review — Counter_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_65`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 165 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 166 | START | 166 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `16` | `15` | 170 | START | 170 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 170 | START | 181 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 170 | START | 170 | 206 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `2` | `1` | 170 | START | 170 | 249 |
| ✅ EXACT | `Action_SnapReceive` | LT | `9` | `8` | 180 | END | 166 | 180 |
| ✅ EXACT | `Action_Handoff` | QB | `1` | `0` | 193 | START | 193 | 209 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 210 | START | 210 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 249 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_Handoff` | 193 | 209 | 17 | inferred_complete_timeline |
| `Action_None` | 210 | 273 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 479 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 330 | 165 | inferred_complete_timeline |
| `Action_None` | 332 | 415 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 347 | 182 | inferred_complete_timeline |
| `Action_None` | 355 | 362 | 8 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 170 | 249 | 80 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 256 | 357 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_SnapReceive` | 166 | 180 | 15 | inferred_complete_timeline |
| `Action_None` | 181 | 327 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 189 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 196 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_BallSnap` | 166 | 180 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 191 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 241 | 46 | inferred_complete_timeline |
| `Action_None` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 318 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 235 | 70 | inferred_complete_timeline |
| `Action_None` | 238 | 258 | 21 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 288 | 123 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 199 | 34 | inferred_complete_timeline |
| `Action_None` | 210 | 339 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 321 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 479 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 233 | 68 | inferred_complete_timeline |
| `Action_None` | 242 | 282 | 41 | inferred_complete_timeline |
| `Action_None` | 285 | 294 | 10 | inferred_complete_timeline |
| `Action_None` | 299 | 349 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 479 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 365 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 479 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 330 | 165 | inferred_complete_timeline |
| `Action_None` | 332 | 479 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 241 | 76 | inferred_complete_timeline |
| `Action_None` | 246 | 455 | 210 | inferred_complete_timeline |
| `Action_None` | 457 | 459 | 3 | inferred_complete_timeline |
| `Action_None` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_None` | 166 | 256 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–212 | 213 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–369 | 309 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 12–23 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 197–254 | 58 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 223–325 | 92 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 235–250 | 15 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 247–287 | 41 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 248–334 | 87 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 270–345 | 75 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 296–313 | 17 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 376–479 | 104 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 436–456 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 132: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [166–180], lower_priority='Action_DownBlock' annotated_start=170, effective_Action_DownBlock_start=181.
- ⚠️ Action 'Action_None' range [210-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-357] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-339] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-258] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-330] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-479] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-327] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-455] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-288] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-365] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-330] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-479] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-189] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-479] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-349] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [170-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [215-219] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-369] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-287] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-334] for track '29' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-313] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-441] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-456] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>