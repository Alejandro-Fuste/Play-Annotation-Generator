# Play-Annotation-Generator Annotation Review — Counter_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_40`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | defense | `13` | `12` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 221 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 222 | START | 222 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `11` | `10` | 228 | START | 228 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `3` | 228 | START | 228 | 274 |
| ✅ EXACT | `Action_DownBlock` | RT | `6` | `5` | 228 | START | 228 | 317 |
| ✅ EXACT | `Action_PullBlock` | LG | `2` | `1` | 228 | START | 228 | 279 |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | `13` | `12` | 228 | START | 228 | 317 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `15` | `14` | 230 | START | 230 | 263 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 235 | END | 222 | 235 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 249 | START | 249 | 263 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `14` | 264 | START | 264 | 369 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 317 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_SnapReceive` | 222 | 235 | 14 | inferred_complete_timeline |
| `Action_None` | 236 | 248 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 249 | 263 | 15 | inferred_complete_timeline |
| `Action_None` | 264 | 389 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 230 | 263 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 369 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 325 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 292 | 71 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PullBlock` | 228 | 279 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_BallSnap` | 222 | 235 | 14 | inferred_complete_timeline |
| `Action_None` | 236 | 389 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 274 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 278 | 317 | 40 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 317 | 90 | inferred_complete_timeline |
| `Action_None` | 318 | 341 | 24 | inferred_complete_timeline |
| `Action_None` | 344 | 389 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 389 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 265 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 274 | 317 | 44 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 371 | 150 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 344 | 123 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 228 | 317 | 90 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 365 | 144 | inferred_complete_timeline |
| `Action_None` | 370 | 389 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_None` | 222 | 346 | 125 | inferred_complete_timeline |
| `Action_None` | 351 | 372 | 22 | inferred_complete_timeline |
| `Action_None` | 374 | 389 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 52–270 | 219 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 76–80 | 5 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 268–333 | 10 | 3 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 295–389 | 95 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 309–389 | 79 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 310–389 | 80 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 330–389 | 57 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 335–389 | 46 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 350–355 | 5 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 360–389 | 30 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 364–389 | 26 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 32 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PullBlock' range [228-279] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-365] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-341] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-346] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-344] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-389] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-371] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-369] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-342] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-349] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-382] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '30' has 1 frames without a visible bounding box.
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

</details>