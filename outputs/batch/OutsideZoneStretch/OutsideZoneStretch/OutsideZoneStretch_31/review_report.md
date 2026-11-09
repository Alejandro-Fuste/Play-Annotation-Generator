# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_31`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `2` | 210 | START | 210 | 254 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 210 | START | 210 | 316 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 210 | START | 210 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 210 | START | 210 | 247 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 261 | START | 261 | 299 |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `17` | `17` | 316 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |
| `Action_PressEdge` | 261 | 299 | 39 | inferred_complete_timeline |
| `Action_None` | 300 | 344 | 45 | inferred_complete_timeline |
| `Action_None` | 353 | 365 | 13 | inferred_complete_timeline |
| `Action_None` | 370 | 539 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 247 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 252 | 302 | 51 | inferred_complete_timeline |
| `Action_None` | 371 | 539 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 254 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 259 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 263 | 271 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 275 | 278 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 316 | 32 | inferred_complete_timeline |
| `Action_None` | 317 | 333 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 316 | 107 | inferred_complete_timeline |
| `Action_None` | 317 | 539 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 278 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 316 | 31 | inferred_complete_timeline |
| `Action_None` | 317 | 319 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 164 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 240 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 267 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 289 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 333 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 358 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 539 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 332 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 539 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 479 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 501 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 527 | 539 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–256 | 257 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 60–91 | 32 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 111–140 | 6 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 119–133 | 13 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 151–256 | 104 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 160–539 | 368 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 264–539 | 270 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 267–539 | 268 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 274–277 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 275–529 | 187 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 285–539 | 253 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 294–539 | 235 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 296–332 | 37 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 315–539 | 212 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 320–478 | 159 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 344–412 | 69 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 383–386 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 394–539 | 141 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 399–458 | 60 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 407–539 | 104 | 6 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 417–472 | 18 | 4 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 428–539 | 101 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 436–539 | 102 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 439–505 | 62 | 2 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 441–457 | 12 | 2 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 451–466 | 5 | 2 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 454–539 | 73 | 4 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 455–466 | 9 | 2 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 468–482 | 15 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 500–521 | 5 | 2 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 515–539 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `17` (Position_Unknown)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 107 frames exceeds threshold 90 frames [start=210, end=316].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 107 frames exceeds threshold 90 frames [start=210, end=316].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 107 frames exceeds threshold 90 frames [start=210, end=316].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 107 frames exceeds threshold 90 frames [start=210, end=316].
- ⚠️ Segment 'Action_Handoff' for track '17' has invalid range: start=316, end=91. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [263-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [275-278] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [252-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-365] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-539] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-240] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-333] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-359] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-332] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-539] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-355] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-479] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-501] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-358] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-539] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-320] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-447] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-452] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-539] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-516] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-522] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-526] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-529] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-330] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-346] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-539] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-488] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-411] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-478] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-412] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-532] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [538-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-458] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-437] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-471] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-485] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-425] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-445] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-472] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-444] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-539] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-446] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-539] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-498] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-505] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-448] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-457] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-452] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-466] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-456] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-479] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-520] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-461] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-466] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-482] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-502] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-521] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>