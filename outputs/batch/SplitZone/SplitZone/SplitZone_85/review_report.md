# Play-Annotation-Generator Annotation Review — SplitZone_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_85`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 24 | START | 25 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 24 | START | 25 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 24 | START | 25 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 24 | START | 25 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 24 | START | 25 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 24 | START | 25 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 24 | START | 25 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 24 | START | 25 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 24 | START | 25 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 24 | START | 25 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 24 | START | 25 | 209 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 210 | START | 210 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 213 | START | 213 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 213 | START | 246 | 266 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 213 | START | 213 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 213 | START | 213 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `8` | 213 | START | 213 | 253 |
| ✅ EXACT | `Action_SplitBlock` | HB | `7` | `7` | 221 | START | 221 | 311 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 231 | END | 210 | 231 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 235 | START | 235 | 239 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `13` | 240 | START | 240 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 311 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 25–244
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_SnapReceive` | 210 | 231 | 22 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 239 | 215 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 389 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 220 | 196 | inferred_complete_timeline |
| `Action_SplitBlock` | 221 | 311 | 91 | inferred_complete_timeline |
| `Action_None` | 312 | 389 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 298 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–268
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 212 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 253 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 268 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 212 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 311 | 99 | inferred_complete_timeline |
| `Action_None` | 312 | 389 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 25–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_BallSnap` | 210 | 222 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 266 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 212 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 232 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 252 | 262 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 290 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 292 | 311 | 20 | inferred_complete_timeline |
| `Action_None` | 312 | 389 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 25–389
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 212 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 293 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 295 | 311 | 17 | inferred_complete_timeline |
| `Action_None` | 312 | 376 | 65 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 263 | 54 | inferred_complete_timeline |
| `Action_None` | 267 | 270 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 293 | 15 | inferred_complete_timeline |
| `Action_None` | 297 | 389 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–291
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 234 | 25 | inferred_complete_timeline |
| `Action_None` | 239 | 286 | 48 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 238 | 29 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |
| `Action_None` | 277 | 338 | 62 | inferred_complete_timeline |
| `Action_None` | 340 | 389 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 225 | 16 | inferred_complete_timeline |
| `Action_None` | 231 | 250 | 20 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 389 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 267 | 58 | inferred_complete_timeline |
| `Action_None` | 270 | 389 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 275 | 66 | inferred_complete_timeline |
| `Action_None` | 278 | 389 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 273 | 64 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 25–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 209 | 185 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 171–385 | 82 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 253–369 | 117 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 270–275 | 6 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 276–389 | 110 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 286–385 | 100 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 292–389 | 98 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 323–389 | 67 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 341–346 | 6 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [210–231], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=232.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
- ⚠️ Action 'Action_None' range [210-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-338] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-376] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [264-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [252-262] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [264-265] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-389] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 240, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [240-244] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [210-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [246-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-209] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-369] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-385] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '30' has 1 frames without a visible bounding box.
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

</details>