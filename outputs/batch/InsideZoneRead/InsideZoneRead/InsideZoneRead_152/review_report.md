# Play-Annotation-Generator Annotation Review — InsideZoneRead_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_152`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 10
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `23` | `22` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `4` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | defense | `3` | `2` |
| ✅ EXACT | `Action_ReadDefender` | CB1 | defense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 82 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `11` | `10` | 99 | START | 99 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `16` | 102 | START | 102 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `18` | 102 | START | 102 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `20` | 102 | START | 102 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `23` | `22` | 102 | START | 102 | 195 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `4` | `3` | 111 | END | 99 | 111 |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | `3` | `2` | 113 | START | 113 | 195 |
| ✅ EXACT | `Action_ReadDefender` | CB1 | `4` | `3` | 117 | START | 117 | 128 |
| ✅ EXACT | `Action_Handoff` | CB1 | `4` | `3` | 129 | START | 129 | 140 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `7` | `6` | 141 | START | 141 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 195 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 265 | 167 | inferred_complete_timeline |
| `Action_None` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 314 | 37 | inferred_complete_timeline |
| `Action_None` | 335 | 338 | 4 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 323 | 225 | inferred_complete_timeline |
| `Action_None` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 195 | 94 | inferred_complete_timeline |
| `Action_None` | 196 | 226 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 195 | 94 | inferred_complete_timeline |
| `Action_None` | 196 | 229 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 82–244
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 195 | 94 | inferred_complete_timeline |
| `Action_None` | 196 | 234 | 39 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 195 | 94 | inferred_complete_timeline |
| `Action_None` | 196 | 235 | 40 | inferred_complete_timeline |
| `Action_None` | 237 | 327 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 233 | 122 | inferred_complete_timeline |
| `Action_None` | 235 | 359 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 113 | 195 | 83 | inferred_complete_timeline |
| `Action_None` | 196 | 279 | 84 | inferred_complete_timeline |
| `Action_None` | 282 | 359 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 310 | 212 | inferred_complete_timeline |
| `Action_None` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 359 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 140 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 359 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 302 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–359 | 354 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–359 | 359 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–16 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 243–265 | 23 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 262–353 | 65 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 285–314 | 15 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 287–359 | 72 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 302–359 | 58 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 332–359 | 25 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 6 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 303: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 304: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '22' (RG) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
- ⚠️ Action 'Action_None' range [196-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-265] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-323] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-234] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-327] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-321] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-353] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-295] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-301] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_152'; source metadata written as null.

</details>