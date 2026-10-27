# Play-Annotation-Generator Annotation Review — Counter_386

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_386`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 81
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 220 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 221 | START | 221 | 234 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `17` | `16` | 224 | START | 235 | 320 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `19` | 224 | START | 224 | 256 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `4` | `3` | 224 | START | 224 | 320 |
| ✅ EXACT | `Action_PullBlock` | RG | `16` | `15` | 224 | START | 224 | 320 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `18` | `17` | 224 | START | 224 | 286 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 234 | END | 221 | 234 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 247 | START | 247 | 271 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 272 | START | 272 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 320 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_SnapReceive` | 221 | 234 | 14 | inferred_complete_timeline |
| `Action_None` | 235 | 246 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 247 | 271 | 25 | inferred_complete_timeline |
| `Action_None` | 272 | 297 | 26 | inferred_complete_timeline |
| `Action_None` | 300 | 389 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 389 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 243 | 23 | inferred_complete_timeline |
| `Action_None` | 245 | 247 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 220 | 111 | inferred_complete_timeline |
| `Action_None` | 221 | 294 | 74 | inferred_complete_timeline |
| `Action_None` | 304 | 389 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 224 | 286 | 63 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 293 | 320 | 28 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 256 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 279 | 22 | inferred_complete_timeline |
| `Action_None` | 340 | 389 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_BallSnap` | 221 | 234 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 320 | 86 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_PullBlock` | 224 | 320 | 97 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 278 | 58 | inferred_complete_timeline |
| `Action_None` | 292 | 334 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 276 | 56 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 285 | 65 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 220 | 92 | inferred_complete_timeline |
| `Action_None` | 221 | 279 | 59 | inferred_complete_timeline |
| `Action_None` | 281 | 389 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 304 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_None` | 221 | 300 | 80 | inferred_complete_timeline |
| `Action_None` | 302 | 389 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–389 | 390 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 263–389 | 102 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 274–389 | 112 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 278–389 | 109 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 280–389 | 97 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 303–389 | 87 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 314–389 | 76 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 341–389 | 49 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 344–389 | 46 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | 136 | 172 | 16 | 43.2% | 139–152, 156–162 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `17` (C): Annotated start 224 != Inferred start 235
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 774: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (Unknown) duration 97 frames exceeds threshold 90 frames [start=224, end=320].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '15' (RG) duration 97 frames exceeds threshold 90 frames [start=224, end=320].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 97 frames exceeds threshold 90 frames [start=224, end=320].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [221–234], lower_priority='Action_DownBlock' annotated_start=224, effective_Action_DownBlock_start=235.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LT) duration 97 frames exceeds threshold 90 frames [start=224, end=320].
- ⚠️ Action 'Action_None' range [221-300] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-278] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-334] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-304] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-297] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-389] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [224-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [289-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [258-279] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-293] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-323] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>