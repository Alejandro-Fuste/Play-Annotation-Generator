# Play-Annotation-Generator Annotation Review — Counter_390

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_390`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 165 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `14` | `13` | 121 | START | 121 | 123 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `14` | `13` | 124 | START | 124 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 124 | START | 124 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 124 | START | 124 | 172 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `15` | `14` | 124 | START | 124 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 134 | END | 121 | 134 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 143 | START | 143 | 165 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `8` | 166 | START | 166 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 134 | 14 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 143 | 165 | 23 | inferred_complete_timeline |
| `Action_None` | 166 | 360 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 182 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 179 | 59 | inferred_complete_timeline |
| `Action_None` | 188 | 268 | 81 | inferred_complete_timeline |
| `Action_None` | 272 | 382 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 194 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 212 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 172 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 194 | 230 | 37 | inferred_complete_timeline |
| `Action_None` | 263 | 287 | 25 | inferred_complete_timeline |
| `Action_None` | 290 | 330 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 220 | 100 | inferred_complete_timeline |
| `Action_None` | 222 | 319 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 201 | 81 | inferred_complete_timeline |
| `Action_None` | 203 | 327 | 125 | inferred_complete_timeline |
| `Action_None` | 329 | 357 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 389 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 219 | 99 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |
| `Action_None` | 241 | 249 | 9 | inferred_complete_timeline |
| `Action_None` | 253 | 370 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 241 | 121 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 273 | 17 | inferred_complete_timeline |
| `Action_None` | 275 | 282 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–387
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 249 | 129 | inferred_complete_timeline |
| `Action_None` | 252 | 387 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 182 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–389 | 383 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 3–366 | 363 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 60–148 | 89 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 77–387 | 311 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 148–389 | 234 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 187–342 | 156 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 226–389 | 164 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 247–387 | 141 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 251–389 | 139 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 260–389 | 129 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 284–298 | 15 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 291–331 | 16 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 294–298 | 5 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 310–371 | 62 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 323–357 | 21 | 5 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 328–346 | 11 | 3 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 337–339 | 3 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 341–389 | 49 | 1 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 344–382 | 14 | 4 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 349–351 | 3 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 352–360 | 5 | 2 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 380–388 | 9 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 782: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 108 frames exceeds threshold 90 frames [start=124, end=231].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (Unknown) duration 108 frames exceeds threshold 90 frames [start=124, end=231].
- ⚠️ Action 'Action_None' range [121-201] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-327] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-357] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-387] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-172] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-330] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-194] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [143-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-268] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-382] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-249] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-366] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [124-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-231] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-342] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-387] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-304] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-298] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-302] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-371] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-352] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-351] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-388] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>