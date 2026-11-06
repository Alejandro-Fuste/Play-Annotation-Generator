# Play-Annotation-Generator Annotation Review — OutsideZoneRead_50

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_50`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 159
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB2 | defense | `10` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR4 | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | WR4 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 365 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB2 | `10` | `10` | 187 | START | 187 | 230 |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR4 | `4` | `4` | 190 | START | 190 | 204 |
| ✅ EXACT | `Action_Handoff` | WR4 | `4` | `4` | 205 | START | 205 | 214 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 223 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 245 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 287 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 389 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 365 | 366 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 389 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 215 | 389 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 185 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 207 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 359 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 366 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 375 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PressEdge` | 187 | 230 | 44 | inferred_complete_timeline |
| `Action_PressEdge` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 274 | 17 | inferred_complete_timeline |
| `Action_None` | 276 | 287 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 318 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 389 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 389 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 3–135 | 65 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–389 | 332 | 6 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 97–245 | 55 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 101–122 | 22 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 103–224 | 33 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 103–389 | 114 | 10 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 103–115 | 13 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 215–223 | 9 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 217–221 | 5 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 232–389 | 158 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 241–389 | 130 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 265–389 | 111 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 266–358 | 83 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 267–389 | 117 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 272–389 | 113 | 4 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 297–380 | 68 | 4 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 302–385 | 51 | 7 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 313–389 | 77 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 319–360 | 37 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 325–389 | 61 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 331–351 | 15 | 4 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 334–389 | 56 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 356–358 | 3 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 356–362 | 7 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 373–389 | 15 | 2 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 379–382 | 4 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'OL' for action 'Action_ZoneBlock' at frame 186 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 98 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-365] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-223] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-245] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-318] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-324] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [187-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 258, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [258-274] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-287] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-185] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-366] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-223] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-257] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-122] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-224] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-223] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-315] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-115] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-223] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-221] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-296] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-304] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-339] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-358] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-366] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-333] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-310] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-345] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-380] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-347] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-374] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-379] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-385] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-324] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-340] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-360] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-389] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-384] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-335] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-345] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-362] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-381] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-382] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>