# Play-Annotation-Generator Annotation Review — SplitZone_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_207`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 24 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 24 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 24 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 24 | START | 25 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 24 | START | 25 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 24 | START | 25 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 24 | START | 25 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 24 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 24 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 24 | START | 25 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `10` | 163 | START | 163 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 166 | START | 176 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 166 | START | 166 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 166 | START | 166 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 166 | START | 166 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `2` | `2` | 171 | START | 171 | 207 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 175 | END | 163 | 175 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 180 | START | 180 | 189 |
| ✅ EXACT | `Action_BallCarry` | RB | `18` | `18` | 190 | START | 190 | 419 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 269 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–313
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 180 | 189 | 10 | inferred_complete_timeline |
| `Action_None` | 190 | 190 | 1 | inferred_complete_timeline |
| `Action_None` | 193 | 313 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 25–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 189 | 165 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 419 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–366
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 366 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 25–327
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 324 | 162 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 25–216
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 216 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–351
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 170 | 146 | inferred_complete_timeline |
| `Action_SplitBlock` | 171 | 207 | 37 | inferred_complete_timeline |
| `Action_SplitBlock` | 219 | 269 | 51 | inferred_complete_timeline |
| `Action_None` | 270 | 351 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–374
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 165 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 220 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 269 | 35 | inferred_complete_timeline |
| `Action_None` | 270 | 374 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 25–179
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 165 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–375
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_BallSnap` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 175 | 175 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 176 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 269 | 91 | inferred_complete_timeline |
| `Action_None` | 270 | 375 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 25–199
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 165 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 191 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 199 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–411
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 52 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 162 | 73 | inferred_complete_timeline |
| `Action_None` | 163 | 191 | 29 | inferred_complete_timeline |
| `Action_None` | 205 | 411 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–261
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_None` | 200 | 261 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–409
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 409 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 25–404
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 404 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 25–375
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 375 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 25–372
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 233 | 71 | inferred_complete_timeline |
| `Action_None` | 239 | 372 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 419 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 419 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–402
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 260 | 98 | inferred_complete_timeline |
| `Action_None` | 269 | 402 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 302 | 140 | inferred_complete_timeline |
| `Action_None` | 305 | 419 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–391
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 301 | 139 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 391 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 25–380 | 347 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 221–365 | 136 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 236–248 | 13 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 243–419 | 166 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 268–405 | 138 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 270–285 | 9 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 274–419 | 146 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 292–314 | 11 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 301–308 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 416: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 104 frames exceeds threshold 90 frames [start=166, end=269].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 104 frames exceeds threshold 90 frames [start=166, end=269].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [163–175], lower_priority='Action_ZoneBlock' annotated_start=166, effective_Action_ZoneBlock_start=176.
- ⚠️ Action 'Action_None' range [163-324] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [171-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-351] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-366] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-72] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-411] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-402] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-409] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-391] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 190, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [190-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-374] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [163-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '10' starts at frame 176, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [176-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-375] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-419] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-372] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [197-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-419] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-380] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-404] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-365] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-405] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '29' has 1 frames without a visible bounding box.
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

</details>